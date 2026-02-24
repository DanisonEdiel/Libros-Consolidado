import json
import re
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_PATH = DATA_DIR / "sri_excel_nombres_index.json"

# Debe mantenerse alineado con SRI_EXCEL_FILES en index.html
SRI_EXCEL_FILES_ORDER = [
    "AZUAY SRI.xlsx",
    "BOLIVAR SRI.xlsx",
    "CARCHI SRI.xlsx",
    "CA\u00d1AR SRI.xlsx",
    "CHIMBORAZO SRI.xlsx",
    "COTOPAXI SRI.xlsx",
    "EL ORO SRI.xlsx",
    "ESMERALDAS SRI.xlsx",
    "GALAPAGOS SRI.xlsx",
    "GUAYAS SRI.xlsx",
    "IMBABURA SRI.xlsx",
    "LOJA SRI.xlsx",
    "LOS RIOS SRI.xlsx",
    "MORONA SANTIAGO SRI.xlsx",
    "NAPO SRI.xlsx",
    "ORELLANA SRI.xlsx",
    "SANTA ELENA SRI.xlsx",
    "SANTO DOMINGO SRI.xlsx",
    "SUCUMBIOS SRI.xlsx",
    "TUNGURAHUA SRI.xlsx",
    "ZAMORA CHINCHIPE SRI.xlsx",
    "santa elena.xlsx",
]

NS_MAIN = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
NS_REL_ATTR = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_PKG_REL = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}


def strip_accents(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", text)
        if unicodedata.category(ch) != "Mn"
    )


def normalize_text(value) -> str:
    text = strip_accents(str(value or "")).strip().lower()
    return re.sub(r"\s+", " ", text)


def normalize_provincia(value) -> str:
    return strip_accents(str(value or "")).strip().upper()


def normalize_name(value) -> str:
    text = normalize_text(value)
    text = re.sub(r"[\"'`´‘’“”]", "", text)
    text = re.sub(r"[.,;:(){}\[\]/\\|_-]+", " ", text)
    text = text.replace("&", " y ")
    text = re.sub(
        r"\b(s\.?\s*a\.?\s*s?\.?|cia\.?|compania|companias?|ltda\.?|ep|e\.?p\.?|sucursal|matriz|agencia|establecimiento)\b",
        " ",
        text,
    )
    return re.sub(r"\s+", " ", text).strip()


def normalize_filename(value) -> str:
    return normalize_text(value)


def col_letters(cell_ref: str) -> str:
    match = re.match(r"([A-Z]+)", cell_ref or "")
    return match.group(1) if match else ""


def read_shared_strings(zf: zipfile.ZipFile):
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    values = []
    for si in root.findall(".//x:si", NS_MAIN):
        text = "".join((t.text or "") for t in si.findall(".//x:t", NS_MAIN))
        values.append(text)
    return values


def get_cell_value(cell: ET.Element, shared_strings):
    ctype = cell.attrib.get("t")
    if ctype == "inlineStr":
        return "".join((t.text or "") for t in cell.findall(".//x:t", NS_MAIN))

    v = cell.find("x:v", NS_MAIN)
    if v is None:
        return ""
    raw = v.text or ""
    if ctype == "s":
        try:
            return shared_strings[int(raw)]
        except Exception:
            return ""
    return raw


def workbook_sheet_paths(zf: zipfile.ZipFile):
    workbook = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map = {
        rel.attrib.get("Id"): rel.attrib.get("Target", "")
        for rel in rels.findall(".//r:Relationship", NS_PKG_REL)
    }
    paths = []
    for sheet in workbook.findall(".//x:sheets/x:sheet", NS_MAIN):
        rid = sheet.attrib.get(f"{{{NS_REL_ATTR}}}id") or sheet.attrib.get("r:id")
        target = rel_map.get(rid, "")
        if not target.startswith("worksheets/"):
            continue
        paths.append(("xl/" + target).replace("\\", "/"))
    return paths


def parse_excel_file(path: Path, accum):
    with zipfile.ZipFile(path) as zf:
        shared_strings = read_shared_strings(zf)
        for sheet_path in workbook_sheet_paths(zf):
            try:
                root = ET.fromstring(zf.read(sheet_path))
            except KeyError:
                continue

            rows = root.findall(".//x:sheetData/x:row", NS_MAIN)
            if len(rows) < 2:
                continue

            headers = {}
            for cell in rows[0].findall("x:c", NS_MAIN):
                headers[col_letters(cell.attrib.get("r", ""))] = str(get_cell_value(cell, shared_strings) or "").strip().upper()

            prov_col = next(
                (col for col, h in headers.items() if h in ("DESCRIPCION_PROVINCIA_EST", "DESCRIPCION_PROVINCIA")),
                None,
            )
            if not prov_col:
                continue

            name_cols = []
            for target in (
                "NOMBRE_FANTASIA_COMERCIAL",
                "MOMBRE_FANTASIA_COMERCIAL",
                "NOMBRE_FANTASIA",
                "NOMBRE_COMERCIAL",
                "RAZON_SOCIAL",
            ):
                for col, h in headers.items():
                    if h == target and col not in name_cols:
                        name_cols.append(col)

            for row in rows[1:]:
                values = {}
                for cell in row.findall("x:c", NS_MAIN):
                    col = col_letters(cell.attrib.get("r", ""))
                    if col == prov_col or col in name_cols:
                        values[col] = get_cell_value(cell, shared_strings)

                provincia = normalize_provincia(values.get(prov_col, ""))
                if not provincia:
                    continue

                nombre_raw = ""
                for col in name_cols:
                    val = values.get(col, "")
                    if str(val).strip():
                        nombre_raw = val
                        break

                nombre = normalize_name(nombre_raw)

                bucket = accum[provincia][path.name]
                bucket["filas"] += 1
                if nombre:
                    bucket["nombres"].add(nombre)


def resolve_input_files():
    by_norm_name = {normalize_filename(p.name): p for p in DATA_DIR.glob("*.xlsx")}
    files = []
    missing = []
    for wanted in SRI_EXCEL_FILES_ORDER:
        p = by_norm_name.get(normalize_filename(wanted))
        if p is None:
            missing.append(wanted)
            continue
        files.append(p)
    return files, missing


def build_index():
    files, missing = resolve_input_files()
    temp = defaultdict(lambda: defaultdict(lambda: {"filas": 0, "nombres": set()}))

    for path in files:
        parse_excel_file(path, temp)

    provincias = {}
    for provincia, by_file in temp.items():
        candidatos = sorted(
            (
                {
                    "archivo": archivo,
                    "filas": data["filas"],
                    "nombres_set": data["nombres"],
                }
                for archivo, data in by_file.items()
            ),
            key=lambda x: x["filas"],
            reverse=True,
        )
        if not candidatos:
            continue

        mejor = candidatos[0]
        filas_totales = sum(c["filas"] for c in candidatos)
        provincias[provincia] = {
            "archivo": mejor["archivo"],
            "filasFuente": mejor["filas"],
            "filasTotalesDetectadas": filas_totales,
            "fuentesDetectadas": len(candidatos),
            "parcial": mejor["filas"] < 50,
            "nombres": sorted(mejor["nombres_set"]),
        }

    return {
        "version": 1,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "files": SRI_EXCEL_FILES_ORDER,
        "missingFiles": missing,
        "provincias": provincias,
    }


def main():
    index = build_index()
    OUTPUT_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    total_nombres = sum(len((p.get("nombres") or [])) for p in index.get("provincias", {}).values())
    print("archivo_salida:", OUTPUT_PATH)
    print("provincias:", len(index.get("provincias", {})))
    print("nombres_totales:", total_nombres)
    if index.get("missingFiles"):
        print("faltantes:", ", ".join(index["missingFiles"]))
    else:
        print("faltantes: ninguno")


if __name__ == "__main__":
    main()
