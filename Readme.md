# **Libros Ecuador 2025**

Plataforma de comparación de precios de libros con mapa interactivo que integra datos reales de librerías y registros oficiales del SRI (2025).

---

## **Características principales**

- Comparación automática de precios entre librerías
- Mapa interactivo (Google Maps + SRI) con cobertura real del mercado
- Funciona **100 % offline** después de la primera carga
- Tablas con carga progresiva (10 en 10)
- Buscador avanzado con filtros por precio, librería y disponibilidad

---

## **Cobertura real del mercado (2025)**

El análisis combina datos oficiales del SRI y la geolocalización real en Google Maps para revelar la verdadera visibilidad digital del sector.

```mermaid
graph TD
    A[Total establecimientos SRI] -->|2.305| B(Registrados oficialmente)
    B -->|737| C{Librerías geolocalizadas<br/>en Google Maps}
    B -->|1.568| D[Establecimientos sin<br/>presencia digital]
    C -->|32%| E[Cobertura digital real]
    D -->|68%| F[Oportunidad de mercado no explotada]

    style A fill:#dc2626,stroke:#991b1b,color:white
    style C fill:#3b82f6,stroke:#1e40af,color:white
    style D fill:#ef4444,stroke:#991b1b,color:white
    style E fill:#f59e0b,stroke:#d97706,color:white
```

```mermaid
flowchart LR
    subgraph Realidad Oficial [Datos Oficiales SRI 2025]
        A[2.305 establecimientos]
        B[65 zonas registradas]
        C[3 zonas con más de 150 est.]
    end

    subgraph Realidad Digital [Google Maps 2025]
        D[737 librerías geolocalizadas]
        E[32% de visibilidad real]
    end

    A -->|Solo 32% visibles| D
    A -->|68% fuera del radar| F[1.568 sin presencia digital]

    style A fill:#dc2626,color:white
    style D fill:#3b82f6,color:white
    style E fill:#f59e0b,color:white
    style F fill:#ef4444,color:white
```

---

## **Tecnologías utilizadas**

| Tecnología                         | Función principal                                 |
| ---------------------------------- | ------------------------------------------------- |
| **HTML5 + CSS3 + JavaScript puro** | Interfaz, lógica de búsqueda y render dinámico    |
| **Leaflet.js**                     | Mapa interactivo con niveles de zoom y marcadores |
| **OpenStreetMap**                  | Capa base gratuita, rápida y ligera               |
| **LocalStorage**                   | Caché local para funcionar sin conexión           |
| **Font Awesome 6**                 | Iconografía moderna y liviana                     |
| **JSON locales**                   | Persistencia de todos los datos sin servidor      |

❗ **No requiere servidor, backend ni base de datos. Todo funciona localmente.**

---

## **Archivos de datos incluidos**

| Archivo                                               | Contenido                                    | Fuente                            |
| ----------------------------------------------------- | -------------------------------------------- | --------------------------------- |
| `librerias_procesadas.json`                           | Más de **28.000 precios reales de libros**   | Scraping propio (2025)            |
| `libros_imagenes.json`                                | Portadas de los libros más buscados          | Catálogos públicos                |
| `librerias_ecuador_pichincha_pastaza_intermedia.json` | 737 librerías geolocalizadas (datos exactos) | Google Maps + Places API          |
| `sri_pichincha_pastaza_coordenadas.json`              | 2.305 establecimientos oficiales SRI (2025)  | Servicio de Rentas Internas (SRI) |

---

## **Resultados del análisis (2025)**

| Métrica                         | Valor      |
| ------------------------------- | ---------- |
| Libros únicos detectados        | **510**    |
| Precio promedio                 | **$20.94** |
| Precio más bajo                 | **$2.49**  |
| Precio más alto                 | **$120**   |
| Librerías geolocalizadas (Maps) | **737**    |
| Zonas registradas por el SRI    | **65**     |
| Total de establecimientos SRI   | **2.305**  |
| Cobertura digital (Maps vs SRI) | **32 %**   |

➡️ _Solo 1 de cada 3 establecimientos oficiales aparece realmente en Google Maps._

---

## **Top 10 zonas con más establecimientos (SRI 2025)**

| #   | Zona / Parroquia         | Establecimientos |
| --- | ------------------------ | ---------------- |
| 1   | **Sangolquí**            | 218              |
| 2   | **Iñaquito**             | 193              |
| 3   | **San Juan**             | 172              |
| 4   | **La Magdalena**         | 127              |
| 5   | **Jipijapa**             | 111              |
| 6   | **San Rafael**           | 103              |
| 7   | **Cotocollao**           | 99               |
| 8   | **Calderón (Carapungo)** | 91               |
| 9   | **Tumbaco**              | 86               |
| 10  | **Conocoto**             | 80               |

---

## **Cómo usar la plataforma**

1. Descarga o clona el repositorio
2. Abre `index.html` en cualquier navegador moderno
3. La primera carga descarga todos los datos (1–5 min)
4. Desde la segunda visita, funciona **instantáneamente y sin internet**

---
