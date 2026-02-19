UNIVERSIDAD CENTRAL DEL ECUADOR
 
Sistema de Análisis del Sector de Librerías en las provincias de Ecuador mediante Revisión Sistemática de Datos y Modelado Heurístico
Jefferson Albuja | Universidad Central del Ecuador, UCE – Ecuador
Cristian Alemán | Universidad Central del Ecuador, UCE – Ecuador  
Carlos Bohórquez | Universidad Central del Ecuador, UCE – Ecuador
Edison Campaña | Universidad Central del Ecuador, UCE – Ecuador 
Katherine Cacuango | Universidad Central del Ecuador, UCE – Ecuador 
Priscila Chisag | Universidad Central del Ecuador, UCE – Ecuador
Andy Galarza | Universidad Central del Ecuador, UCE – Ecuador 
Kevin Lema | Universidad Central del Ecuador, UCE – Ecuador
Edison Llano | Universidad Central del Ecuador, UCE – Ecuador 
Abel López | Universidad Central del Ecuador, UCE – Ecuador
Jefferson Marcalla | Universidad Central del Ecuador, UCE – Ecuador 
Alex Morales | Universidad Central del Ecuador, UCE – Ecuador
Jordan Paida | Universidad Central del Ecuador, UCE – Ecuador 
David Yascaribay | Universidad Central del Ecuador, UCE – Ecuador
Josue Barrera | Universidad Central del Ecuador, UCE – Ecuador
Daniel Clavijo | Universidad Central del Ecuador, UCE – Ecuador


KEYWORDS
Bookstores; book trade; cultural economy; informality; digital data; tax records; territorial inequality; Ecuador.	ABSTRACT
This study examines the structure and performance of the formal bookstore sector across Ecuador’s 24 provinces by integrating administrative tax records with digital geospatial data. Using a Systematic Data Review protocol and a reproducible ETL pipeline developed in Python, the research validates operational establishments, identifies inconsistencies in fiscal registries, and applies a heuristic model to estimate purchasing probability and relative commercial performance based on category positioning, digital frequency, and normalized price. Results show strong urban concentration, significant territorial disparities, and notable gaps between registered and actual activity. The analysis of foreign trade data further confirms a structurally deficit trade balance, reflecting high dependence on imported books and limited national production. Findings demonstrate the technical and legal feasibility of combining public administrative and digital sources to evaluate culturally relevant markets characterized by informality and limited statistical transparency, offering a replicable framework for cultural and regional economic analysis.
PALABRAS CLAVE
Librerías; comercio del libro; economía cultural; informalidad comercial; datos digitales; registros tributarios; desigualdad territorial; Ecuador.	RESUMEN
Este estudio analiza la estructura y el desempeño del sector formal de librerías en las 24 provincias del Ecuador mediante la integración de registros tributarios administrativos y datos geoespaciales digitales. A través de un protocolo de Revisión Sistemática de Datos y un pipeline ETL reproducible desarrollado en Python, la investigación valida establecimientos operativos, identifica inconsistencias en los catastros fiscales y aplica un modelo heurístico para estimar la probabilidad de compra y el desempeño comercial relativo según categoría, frecuencia digital y precio normalizado. Los resultados evidencian una fuerte concentración urbana, marcadas desigualdades territoriales y brechas entre actividad registrada y actividad real. El análisis del comercio exterior confirma además una balanza comercial deficitaria y una alta dependencia de libros importados. Se demuestra la viabilidad técnica y legal de combinar fuentes administrativas y digitales para evaluar mercados culturales caracterizados por informalidad y limitada transparencia estadística.
	Introducción 
El análisis del comercio minorista de libros constituye un indicador clave para medir tanto la salud cultural como la dinámica económica de una región. En el marco de la economía cultural, los bienes editoriales son considerados activos estratégicos por su contribución al capital simbólico y al desarrollo humano. [33], [31] En varias provincias del Ecuador, la cuantificación precisa de este sector enfrenta desafíos estructurales debido a la carencia de datos centralizados y la discrepancia entre los registros fiscales y la realidad operativa de los negocios. [9], [17] A menudo, los catastros oficiales, como los del Servicio de Rentas Internas (SRI), contienen registros de contribuyentes que, aunque legalmente activos, pueden no tener operaciones físicas vigentes o haber cerrado recientemente sin actualizar su estado tributario. [12]
La presente investigación aborda esta problemática mediante el desarrollo de un sistema de inteligencia de negocios que integra datos fiscales estructurados con información no estructurada obtenida vía web scraping. La integración de registros administrativos con fuentes digitales ha sido reconocida en estudios metodológicos como una estrategia adecuada para mejorar la observabilidad de mercados fragmentados. [10], [24] El sistema implementado permite depurar el catastro nacional, validar la operatividad real de los negocios mediante su presencia digital y aplicar un modelo matemático para estimar su volumen de facturación. [12], [25]
La fundamentación metodológica del estudio se sustenta en una Revisión Sistemática de Datos adaptada a la Ciencia de Datos, ejecutada a través de un flujo automatizado ETL (Extract, Transform, Load). Este enfoque se alinea con los lineamientos propuestos para revisiones sistemáticas y análisis estructurados de información secundaria. [3], [11] Asimismo, la aplicación de técnicas de análisis exploratorio de datos (EDA) fortalece la reproducibilidad técnica del conteo y proporciona un marco riguroso para analizar las disparidades comerciales entre el continente y la región insular. [16]

	 Objetivos Específicos
	Depurar y normalizar el catastro de contribuyentes del SRI filtrando los códigos de actividad económica específicos del sector librero, para establecer una base de datos preliminar de estudio.
	Diseñar un flujo de extracción automatizada (ETL) utilizando scripts en Python que consuman las APIs de Google Places y Books, permitiendo enriquecer la data fiscal con información de validación operativa en tiempo real.
	Visualizar los hallazgos a través de un Dashboard interactivo de acceso público que georreferencie los establecimientos y presente estadísticas descriptivas del catálogo bibliográfico y precios.
2. Marco Teórico y Estado del Arte 
2.1 Economía cultural y comercio del libro
El comercio del libro se inscribe dentro de la economía cultural, un campo que reconoce a los bienes culturales no solo como mercancías sujetas a dinámicas de oferta y demanda, sino como portadores de valor simbólico, educativo y social [33], [31]. A diferencia de otros sectores comerciales, el libro articula dimensiones económicas con procesos de formación intelectual, construcción de identidad y transmisión de conocimiento [33]. En este sentido, las librerías cumplen una función estratégica que trasciende su rol mercantil, actuando como nodos de circulación cultural y como infraestructuras fundamentales para el desarrollo educativo de los territorios [32], [31].
En el contexto ecuatoriano, el mercado del libro refleja con claridad las tensiones entre centralización urbana y periferias con acceso limitado a bienes culturales [9], [34]. La distribución espacial de las librerías no responde únicamente al tamaño poblacional, sino a factores estructurales como la presencia de instituciones educativas, la conectividad logística, el dinamismo económico local y la tradición cultural [25], [29]. Provincias con alta densidad universitaria y administrativa concentran una oferta más diversificada, mientras que en territorios rurales, amazónicos o insulares el libro suele circular a través de canales mixtos o informales [34], [2].
Desde esta perspectiva, el comercio librero opera como un indicador sensible del desarrollo cultural regional [33], [31]. La baja densidad de librerías formales en amplias zonas del país no solo limita el acceso al libro, sino que condiciona los hábitos de lectura y profundiza brechas educativas preexistentes [34], [2]. Por ello, el análisis del sector debe comprenderse como parte de una política cultural más amplia, donde la sostenibilidad económica del mercado del libro se vincula directamente con objetivos de equidad cultural, desarrollo humano y fortalecimiento del ecosistema educativo [31], [33].

2.2 Ontología y Economía de los Bienes Culturales: El Libro como Objeto Dual
La economía de la cultura se fundamenta en la premisa de que los bienes y servicios culturales poseen una naturaleza dual que desafía los modelos económicos neoclásicos convencionales. David Throsby, uno de los pilares de esta disciplina, argumenta que estos bienes no solo portan un valor de cambio o valor económico, sino que son depositarios de un valor cultural intrínseco que es multidimensional y, a menudo, inconmensurable en términos puramente monetarios [33]. Esta dualidad implica que el libro es simultáneamente una mercancía sujeta a las leyes de la oferta y la demanda, y un objeto simbólico esencial para la construcción de identidad, soberanía y diversidad cultural [31], [33].

El valor cultural, según Throsby, se descompone en varios elementos: el valor estético, el valor espiritual, el valor social, el valor histórico y el valor simbólico. En la industria del libro, este valor se manifiesta en la capacidad de las obras para transformar la visión del mundo del lector y fortalecer el capital intelectual de una nación. Desde una perspectiva económica, esta característica clasifica a los libros como "bienes de mérito" (merit goods), cuya producción y consumo generan externalidades positivas que justifican la intervención pública y el diseño de políticas de fomento [33], [30], [31].



Dimensión del Valor	Características en el Sector Librero	Impacto Económico
Valor Económico	Precio de mercado, costos de impresión, logística, márgenes de utilidad.	Generación de PIB, empleo y transacciones comerciales.
Valor Simbólico	Identidad nacional, preservación de lenguas, diversidad de pensamiento.	Construcción de marca país y cohesión social.
Valor de Opción	El deseo del ciudadano de que existan librerías, aunque no las use actualmente.	Justificación de subsidios y exenciones fiscales.
Valor de Legado	El valor de transmitir el conocimiento a futuras generaciones.	Inversión en educación y capital cultural a largo plazo.
Tabla 1: Dimensiones de Valor


La noción de "excepción cultural", surgida en las rondas de negociación del GATT en 1993, refuerza esta posición al sostener que los bienes culturales no deben ser tratados como cualquier otro producto en el mercado internacional [31], [30]. Esta postura es particularmente relevante en Iberoamérica, donde la hegemonía de grandes conglomerados transnacionales ha desplazado a las editoriales locales, generando una pérdida de capacidad endógena de producción. En Ecuador, el fortalecimiento de las librerías independientes es, por lo tanto, una estrategia de resistencia cultural frente a la estandarización del consumo [32], [9].

2.3 El libro en el marco de las industrias culturales y la economía naranja
La evolución conceptual desde las "industrias culturales" hacia la "economía naranja" o "industria creativa" ha permitido integrar el sector editorial en un ecosistema más amplio de creación de valor basado en el talento y la propiedad intelectual [31], [30]. Según el Banco Interamericano de Desarrollo (BID), la economía naranja comprende todas las actividades que permiten que las ideas se transformen en bienes y servicios culturales [31]. El libro se sitúa en el núcleo de esta economía, junto con el cine y la música, siendo uno de los sectores con mayor capacidad de generar derechos de autor y valor agregado intangible.   
Sin embargo, esta centralidad no se traduce necesariamente en sostenibilidad económica. El sector librero opera bajo lo que el Centro Regional para el Fomento del Libro en América Latina y el Caribe (CERLALC) denomina un "mercado de oferta". A diferencia de otros sectores donde la demanda impulsa la producción, en el ecosistema del libro, la existencia de una oferta física (librerías de proximidad) es el motor que genera la demanda. La desaparición de una librería no solo implica la pérdida de un punto de venta, sino la extinción de un espacio de mediación cultural que raramente es recuperado por otros canales [1], [32].

Clasificación de Industrias	Ubicación del Sector Editorial	Componentes Clave
Industrias Culturales Convencionales	Editorial, Libros, Revistas, Cine, Música.	Reproducción técnica y difusión masiva.
Artes y Patrimonio	Literatura, Bibliotecas, Museos, Gastronomía.	Valor histórico y creación original.
Nuevas Industrias Creativas	Software, Videojuegos, Publicidad.	Innovación tecnológica y digital.
Tabla 2: Tipos de Industrias

El modelo de círculos concéntricos de Throsby posiciona a la literatura como una "arte creativa central", mientras que la industria editorial se ubica en el primer círculo de "industrias culturales principales" [33]. Esta distinción es vital para entender la cadena de valor: mientras el autor genera el valor cultural primario, la librería actúa como la interfaz crítica que conecta ese valor con el ciudadano-consumidor. En Ecuador, esta interfaz presenta fracturas territoriales evidentes, donde la concentración urbana de la oferta limita el acceso al libro en zonas periféricas, amazónicas y fronterizas [33], [25].
2.4 Informalidad comercial y registros administrativos
La informalidad constituye un rasgo estructural del comercio minorista en Ecuador, y el sector librero no es una excepción [2], [17]. Una proporción significativa de los establecimientos vinculados al libro opera bajo esquemas híbridos —papelerías, centros de copiado o bazares— donde la venta de libros es secundaria o no se encuentra adecuadamente declarada en los registros fiscales [5], [24]. Esta dinámica genera una brecha persistente entre la realidad operativa del mercado y su representación en los sistemas administrativos [11], [12].
Los registros tributarios, aunque fundamentales para la medición económica, tienden a sobreestimar o distorsionar el tamaño real del sector cuando se utilizan de forma aislada [12], [24]. Es frecuente encontrar contribuyentes clasificados como activos que ya no mantienen operación efectiva, así como establecimientos en funcionamiento que figuran bajo códigos genéricos o no se encuentran formalmente registrados [13], [11]. 
En provincias con menor dinamismo económico, estas inconsistencias se acentúan debido a la alta rotación de pequeños negocios y la fragilidad financiera de los microemprendimientos culturales [26], [18]. La informalidad no solo afecta la recaudación fiscal, sino que debilita la visibilidad del sector y limita el diseño de políticas públicas basadas en evidencia [2], [17]. Asimismo, contribuye a la expansión de mercados paralelos, como la piratería editorial y la reprografía informal, que erosionan la sostenibilidad del comercio formal [1], [8].


Para los sistemas de contabilidad nacional, la informalidad se enmarca dentro de la "Economía No Observada" (ENO). El manual de la OCDE sobre la medición de la ENO identifica cinco categorías principales que deben ser capturadas para garantizar la exhaustividad del Producto Interno Bruto (PIB) [2].   
	Producción Subterránea: Actividades que son legales pero que se ocultan deliberadamente a las autoridades públicas para evitar el pago de impuestos, contribuciones a la seguridad social o el cumplimiento de normas laborales y administrativas. En el sector librero, esto se manifiesta en establecimientos que operan sin registro o que declaran ingresos significativamente menores a los reales.   
	Producción Ilegal: Actividades prohibidas por la ley o que se vuelven ilegales cuando son realizadas por personas no autorizadas. En el ecosistema del libro, la piratería editorial representa la manifestación más crítica de esta categoría.   
	Producción del Sector Informal: Unidades económicas que no están constituidas en sociedad y que pertenecen a hogares, operando a pequeña escala y con bajos niveles de organización. Muchas librerías de barrio y bazares de libros usados en Ecuador encajan en este perfil.   
	Producción de Hogares para Uso Final Propio: Actividades de autoconsumo que quedan fuera del mercado comercial.   
	Producción Omitida por Deficiencias en la Recolección de Datos: Registros administrativos obsoletos o incompletos que no reflejan la apertura de nuevos locales o el cierre de otros.   
En Ecuador, la diferencia entre la oferta registrada fiscalmente en el Servicio de Rentas Internas (SRI) y la oferta real disponible es sustancial. Los catastros oficiales a menudo contienen registros de contribuyentes que, aunque figuran como activos, han cesado sus operaciones o han cambiado de actividad sin actualizar su estado tributario. Asimismo, existe una brecha de "actividad nominal vs. actividad real": muchos negocios registrados bajo códigos CIIU de venta de libros son, en la práctica, papelerías o comercios mixtos donde el libro es un producto marginal [12], [1].
Indicador de Informalidad	Manifestación en Librerías	Consecuencia para el Sector
Subdeclaración de ingresos	Ventas sin comprobante de venta autorizado.	Debilitamiento de la recaudación y competencia desleal.
Uso de códigos CIIU genéricos	Registro como "Bazar" o "Papelería" en lugar de "Librería".	Invisibilidad estadística del sector cultural.
Incumplimiento laboral	Personal sin seguridad social o contratos formales.	Inestabilidad del capital humano especializado.
Piratería editorial	Venta de copias no autorizadas en locales físicos o digitales.	Erosión de los derechos de autor y de la industria legal.
Tabla 3: Parámetros de librerías

2.4 Huella Digital como Proxy de actividad Económica
La expansión de plataformas digitales de geolocalización y comercio electrónico ha generado una nueva capa de información sobre la actividad económica: la huella digital [7], [8]. En sectores caracterizados por alta informalidad y escasa transparencia estadística, esta huella constituye un proxy valioso para inferir la existencia y operatividad de los establecimientos comerciales [10], [2].
En el comercio del libro, la presencia en plataformas digitales permite validar si un negocio registrado mantiene operación efectiva, identificar establecimientos no reflejados adecuadamente en los catastros fiscales y observar patrones de localización espacial [12], [24]. Elementos como direcciones verificadas, horarios de atención y reseñas de usuarios ofrecen señales indirectas pero consistentes sobre la actividad real de una librería [7], [8].
La huella digital no reemplaza a las fuentes administrativas, pero las complementa de manera estratégica. Su integración reduce el sesgo producido por registros desactualizados y amplía el universo observable del sector, incorporando una dimensión dinámica al análisis [10], [11].
Desde una perspectiva metodológica, el uso de información digital como proxy de actividad económica representa un cambio de paradigma en la medición de mercados culturales, permitiendo transitar desde enfoques estáticos hacia modelos híbridos basados en evidencia empírica en tiempo casi real [3], [10]. En contextos como el ecuatoriano, esta aproximación resulta pertinente para auditar sectores fragmentados y territorialmente desiguales [2], [9], proporcionando una base más robusta para la toma de decisiones públicas y el diseño de políticas culturales orientadas a la equidad territorial y al fortalecimiento del mercado formal del libro.

3. Comercio exterior del libro del Ecuador
El análisis del comercio exterior del libro ecuatoriano revela una balanza comercial estructuralmente deficitaria que contextualiza las condiciones del mercado interno estudiado. Según datos del Banco Central del Ecuador y el Servicio Nacional de Aduanas (SENAE), las importaciones de libros superan consistentemente a las exportaciones en una proporción aproximada de 10:1 [27], [38].
3.1 Importaciones
Durante el período 2020-2024, Ecuador importó un promedio anual de 4.2 millones de dólares en material bibliográfico, principalmente desde Colombia (45%), España (23%) y México (18%). Esta dependencia externa afecta directamente la estructura de costos de las librerías locales, especialmente en provincias periféricas como El Oro y Galápagos, donde los márgenes de intermediación se incrementan por costos logísticos adicionales [27], [30].
La partida arancelaria 4901 (Libros, folletos e impresos similares) concentra el 78% del valor importado, mientras que el 22% restante corresponde a material educativo especializado. Las librerías validadas en este estudio reportan tiempos de reposición de inventario de 15-30 días para títulos importados, factor que limita su capacidad de respuesta ante demandas específicas [27], [50].
3.2 Exportaciones y Producción Editorial Nacional
La producción editorial ecuatoriana se concentra en Quito (62%) y Guayaquil (31%), con una participación marginal de otras provincias. Las exportaciones totalizaron aproximadamente USD 380,000 anuales en el período estudiado, destinadas principalmente a mercados de nicho en Estados Unidos y España (literatura ecuatoriana contemporánea y textos académicos especializados) [38], [48], [50].
Esta asimetría comercial explica parcialmente los resultados obtenidos en el modelo heurístico: las librerías ecuatorianas operan fundamentalmente como canales de distribución de contenido foráneo, con márgenes comerciales reducidos que dificultan inversiones en infraestructura digital y promoción [27], [29], [41].
3.3 Impacto en el Mercado Insular
En el caso particular de las Galápagos, la condición de zona especial aduanera genera paradojas comerciales. Si bien el régimen especial exime ciertos productos de aranceles, los costos logísticos de transporte marítimo y aéreo incrementan el precio final de los libros en un 40-60% respecto al continente. Esta barrera explica la menor densidad de establecimientos validados (2 librerías operativas) y su dependencia del mercado turístico para compensar el reducido volumen de ventas al público local [26], [30].

4. Modelo Heurístico: Compra de Libros
El modelo heurístico propuesto se fundamenta en la construcción de una función de puntuación (Score) que combina tres componentes principales: categoría comercial, frecuencia de aparición y precio normalizado.

Se parte del siguiente supuesto:
Un libro tiene mayor probabilidad de compra si:
	Se encuentra en categorías promocionales,
	Aparece con mayor frecuencia en el mercado digital,
	Presenta un precio relativamente accesible.

4.1 Componente 1: Puntaje por Categoría (C)
La variable categoría refleja el nivel de promoción del libro dentro de la plataforma comercial. Se asignaron valores discretos según su relevancia comercial:

Categoría	Puntaje
Más Buscados	5
Destacados	4
Infantil	3
Juvenil	3
General	2

Este componente representa el impacto del posicionamiento estratégico del libro en el mercado nacional.

4.2 Componente 2: Puntaje por Frecuencia de Aparición (F) 
Se calculó la frecuencia absoluta de cada título dentro del dataset:

f_i="N" "u"  ˊ"mero de veces que aparece el título " i

Para evitar un crecimiento desproporcionado del impacto de la frecuencia, se aplicó una transformación logarítmica:
F_i=log⁡(1+f_i)

Este componente representa el nivel de exposición del libro en el mercado digital nacional.

4.3 Componente 3: Puntaje por Precio Normalizado (P)
El precio influye directamente en la decisión de compra. Para estandarizar su impacto, se aplicó una normalización en el rango observado:

P_i=1-(precio_i-precio_min)/(precio_max-precio_min )

Donde:
	precio_mines el precio más bajo del dataset.
	precio_maxes el precio más alto del dataset.
De esta forma:
	Libros más económicos → valores cercanos a 1
	Libros más costosos → valores cercanos a 0

4.4 Función Heurística Final
La función de puntuación total se define como:

Score_i=w_1 C_i+w_2 F_i+w_3 P_i


Donde:
	w_1=0.5  (peso de categoría)
	w_2=0.3  (peso de frecuencia)
	w_3=0.2  (peso de precio)
Sujeto a:
w_1+w_2+w_3=1

El ranking nacional de probabilidad de compra se obtiene ordenando los libros en función de Score_ide mayor a menor.

4.5 Resultados Modelo Heurístico
Los resultados muestran una clara concentración de los valores más altos del Score en libros pertenecientes a la categoría “Más Buscados”, lo que confirma la fuerte influencia del posicionamiento comercial dentro del modelo.
El libro con mayor puntuación heurística fue:
	ARSÈNE LUPIN C, CABALLERO LADRÓN
	Categoría: Más Buscados
	Frecuencia de aparición: 9 registros
	Rango de precios observado: USD 8.20 – 9.96
	Score máximo obtenido: 3.3838
Este resultado se explica por la combinación de:
	Máxima ponderación en la variable categoría.
	Alta frecuencia de aparición en distintas librerías.
	Precio relativamente bajo respecto al rango general del dataset.
En segundo lugar se ubicó:
	MI NOMBRE ES EMILIA DEL VALLE
	Categoría: Más Buscados
	Frecuencia: 7 registros
	Precio: USD 23.50
	Score: 3.3015
A pesar de presentar un precio superior al del primer lugar, su alta frecuencia y pertenencia a una categoría promocional compensaron dicha diferencia. 


5. Pipeline Reproducible de Datos
El presente estudio implementa un pipeline reproducible de datos a escala nacional, diseñado para integrar, depurar, validar y analizar información administrativa, digital y geoespacial relacionada con el comercio formal de librerías en las 24 provincias del Ecuador.
 El pipeline se fundamenta en un enfoque ETL (Extract–Transform–Load), validado empíricamente a través de doce estudios previos desarrollados en diferentes provincias del país, lo que garantiza consistencia metodológica, trazabilidad analítica y posibilidad de replicación en otros contextos territoriales [3], [10].
5.1 Definición de alcance territorial y temporal
El alcance territorial del pipeline es nacional, abarcando las 24 provincias del Ecuador: Azuay, Bolívar, Cañar, Carchi, Chimborazo, Cotopaxi, El Oro, Esmeraldas, Galápagos, Guayas, Imbabura, Loja, Los Ríos, Manabí, Morona Santiago, Napo, Orellana, Pastaza, Pichincha, Santa Elena, Santo Domingo de los Tsáchilas, Sucumbíos, Tungurahua y Zamora Chinchipe.
Esta cobertura territorial se construyó mediante la integración progresiva de los doce estudios analizados, los cuales abarcan provincias de la Costa, Sierra, Amazonía y Región Insular, permitiendo capturar la heterogeneidad geográfica, demográfica y económica del país [5], [11].
El alcance temporal se establece en el período 2024–2025, considerando los registros tributarios más recientes del Servicio de Rentas Internas (SRI) y la información digital obtenida en el mismo intervalo. Esta delimitación temporal garantiza coherencia entre fuentes administrativas y digitales, evitando sesgos derivados de desactualización de datos [5], [7].
5.2 Ingesta, Normalización y Limpieza
La ingesta de datos se realiza desde múltiples fuentes de acceso público, principalmente:
	Registros tributarios oficiales del Servicio de Rentas Internas (SRI).
	Plataformas digitales de localización comercial, principalmente Google Maps.
	Fuentes complementarias derivadas de revisiones sistemáticas de literatura y bases académicas.
Los datos extraídos presentan alta heterogeneidad en formato, estructura y calidad, por lo que se implementa un proceso de normalización y limpieza exhaustiva, que incluye:
	Estandarización de nombres comerciales y razones sociales.
	Normalización de direcciones y campos textuales.
	Eliminación de registros duplicados mediante métricas de similitud textual.
	Depuración de valores nulos, inconsistentes o incompletos.
Este proceso permite consolidar un dataset unificado y homogéneo, condición indispensable para el análisis comparativo entre provincias [3], [10].
5.3 Controles de integridad y validación tributaria
La validación tributaria constituye un componente central del pipeline. Cada registro es contrastado con el estado del contribuyente en el SRI, clasificándolo como activo, suspendido o pasivo [5].
Asimismo, se verifica la coherencia entre la actividad económica declarada (códigos CIIU asociados a la comercialización de libros) y la información observada en plataformas digitales [7]. Este cruce permite identificar:
	Establecimientos formalmente registrados pero inactivos.
	Librerías informales no registradas en el SRI.
	Inconsistencias entre registro tributario y operación real.
Este control reduce significativamente el riesgo de sobreestimación del comercio formal y fortalece la validez del análisis nacional [5], [7].

5.4 Validación espacial y geocodificación
Para garantizar precisión territorial, el pipeline incorpora procesos de geocodificación directa e inversa, transformando direcciones textuales en coordenadas geográficas (latitud y longitud) [7].
Los registros geocodificados son sometidos a validación espacial, verificando que cada punto se encuentre dentro de los límites administrativos provinciales y cantonales correspondientes. Los registros con incoherencias espaciales son corregidos o descartados [10].
Este procedimiento permite construir una base de datos geoespacial confiable, fundamental para análisis territoriales y comparaciones interprovinciales.
5.5 Consideraciones éticas y legales
El pipeline fue diseñado bajo principios de ética, legalidad y transparencia. Toda la información utilizada proviene de fuentes de acceso público y se procesó respetando los términos de uso de las plataformas digitales [9].
No se recolectó ni almacenó información personal sensible, cumpliendo con la Ley Orgánica de Protección de Datos Personales del Ecuador. Asimismo, las técnicas de extracción automatizada incorporan mecanismos de control para evitar sobrecarga de servicios externos.
Las limitaciones derivadas de la naturaleza pública y administrativa de los datos, así como la imposibilidad de medir directamente el comercio ilegal, son reconocidas explícitamente como parte del rigor metodológico del estudio.
6. Resultados Nacionales
La presente sección expone los resultados agregados a escala nacional, obtenidos a partir de la integración de doce estudios provinciales desarrollados bajo un mismo pipeline metodológico. La aplicación uniforme de criterios de filtrado por códigos CIIU, validación tributaria, geocodificación y análisis espacial permite construir una visión comparativa del ecosistema formal de librerías en las 24 provincias del Ecuador, superando las limitaciones de los análisis aislados por territorio [5], [11], [37], [39], [53]. 
Los resultados se presentan en cinco dimensiones: distribución territorial, composición económica, estado de formalidad, concentración espacial e indicadores agregados [14], [15], [19].
6.1 Distribución nacional de librerías por provincia
El análisis revela una distribución territorial marcadamente desigual de las librerías en el Ecuador. La mayor parte de los establecimientos formales dedicados a la venta de libros se concentra en un número reducido de provincias, principalmente aquellas con mayor peso demográfico, educativo y administrativo [11], [26], [30], [36].
Pichincha y Guayas concentran la mayor cantidad de librerías a nivel nacional, actuando como nodos centrales del ecosistema editorial. A estas se suman provincias como Azuay, Tungurahua y Loja, donde la presencia de universidades, instituciones educativas y tradición cultural favorece una mayor densidad relativa de establecimientos [27], [38], [50]
En contraste, provincias amazónicas, fronterizas e insulares presentan una oferta librera limitada y fragmentada. En territorios como Napo, Sucumbíos, Pastaza, Zamora Chinchipe y Galápagos, el número de librerías especializadas es reducido y, en algunos casos, inexistente fuera de las capitales provinciales [26], [30], [36], [39].
Estos resultados evidencian que la distribución de librerías no depende únicamente del tamaño poblacional, sino de factores estructurales como la concentración urbana, la infraestructura educativa, la conectividad logística y la dinámica económica local [30], [36], [48], [49].
6.2 Composición por CIIU
El análisis por códigos de actividad económica (CIIU) muestra que una parte considerable de los establecimientos asociados al sector del libro no corresponde a librerías especializadas. En la mayoría de provincias, predominan los negocios donde el libro es un producto secundario, como papelerías, bazares o comercios mixtos [5], [37], [39].
El código CIIU específico de venta al por menor de libros (G476101) representa una fracción menor del total de establecimientos relacionados con el libro, especialmente fuera de los grandes centros urbanos. En provincias periféricas, la oferta formal se encuentra mayoritariamente diluida en actividades comerciales orientadas a útiles escolares o servicios reprográficos [39], [47].
Esta composición distorsiona las estadísticas oficiales cuando se utilizan únicamente registros administrativos, ya que el número de RUC asociados al libro no refleja necesariamente la disponibilidad real de librerías dedicadas al público lector [5], [11], [51].
6.3 Estado del contribuyente y estructura del sector
La validación cruzada entre el estado tributario del SRI y la evidencia de operación física o digital pone en evidencia una brecha significativa entre registro fiscal y actividad real [5], [7], [12].
A nivel nacional, se identifican numerosos contribuyentes clasificados como activos que no presentan señales actuales de funcionamiento, ya sea por cierre reciente, reconversión del negocio o inactividad prolongada [5], [37], [39]. Esta situación es más frecuente en provincias con menor dinamismo económico y menor fiscalización efectiva [5], [51].
Paralelamente, se detectan establecimientos con operación comercial verificable que no figuran adecuadamente en el catastro fiscal o lo hacen bajo códigos genéricos que no reflejan su actividad principal. Esta doble distorsión —registros activos sin operación y operación sin registro adecuado— configura un sector librero estructuralmente frágil, dominado por microemprendimientos y con baja capacidad de sostenibilidad económica [29], [41], [51].
6.4 Concentración territorial y centralidades
Desde el punto de vista espacial, los resultados muestran una alta concentración de librerías en capitales provinciales y cantones centrales. En la mayoría de provincias analizadas, entre el 70% y el 90% de los establecimientos validados se ubican en uno o dos cantones, generalmente asociados a nodos administrativos, educativos o turísticos [23], [25], [39], [53].
Esta concentración genera extensas áreas sin cobertura formal del libro, particularmente en cantones rurales, zonas amazónicas y territorios de frontera. En estos espacios, el acceso regular a libros depende de ferias temporales, comercio informal o canales digitales no regulados [25], [26].
La evidencia empírica sugiere que esta centralización responde a economías de aglomeración, pero al mismo tiempo reproduce desigualdades territoriales en el acceso a bienes culturales, fenómeno documentado de manera consistente en estudios provinciales previos [25], [26]

7. Limitaciones del estudio
7.1 Limitaciones Metodológicas
Sesgo de Presencia Digital: El protocolo de validación mediante Google APIs excluye establecimientos operativos sin huella digital. Entrevistas informales con comerciantes locales sugieren que al menos el 15-20% de librerías tradicionales en zonas rurales no cuentan con perfiles verificados en plataformas digitales, generando un subregistro sistemático [7] [12].
Temporalidad de los Datos: Los datos del SRI corresponden al último reporte publicado (2024), mientras que la validación digital se realizó en un período de 3 semanas. Establecimientos que cerraron o abrieron durante ventanas temporales entre actualizaciones no fueron capturados [5] [4].




7.2 Limitaciones Técnicas
Cobertura de APIs Google Places API presenta vacíos de información en zonas remotas. Provincias amazónicas mostraron tasas de respuesta nula en el 60% de las consultas iniciales, obligando a implementar búsquedas secundarias por texto libre que incrementan el margen de error [7].
7.3 Limitaciones Contextuales
Exclusión de Canales Informales: El estudio no captura ventas informales en mercados populares, ferias itinerantes o vendedores ambulantes, que según estimaciones del INEC representan el 40% del comercio minorista en Ecuador. Esta omisión subestima significativamente el volumen real de transacciones bibliográficas.

8. Conclusiones
El presente estudio confirma que el sector formal de librerías en el Ecuador presenta una estructura altamente concentrada, territorialmente desigual y metodológicamente subestimada cuando se analiza exclusivamente a partir de registros administrativos. La integración de datos tributarios del SRI con información digital geoespacial permitió evidenciar una brecha significativa entre actividad nominal y actividad operativa real, revelando inconsistencias en el catastro fiscal y la presencia de establecimientos activos sin visibilidad estadística adecuada.
Los resultados demuestran que la distribución nacional de librerías responde a patrones de centralización urbana, donde Pichincha, Guayas y otras provincias con alta densidad educativa concentran la mayor parte del ecosistema formal. En contraste, provincias amazónicas, fronterizas e insulares presentan baja densidad de establecimientos especializados, configurando territorios con acceso limitado al libro como bien cultural.
El modelo heurístico desarrollado permitió estimar probabilidades de compra y desempeño relativo a partir de variables de categoría comercial, frecuencia de aparición y precio normalizado. Si bien no sustituye información contable directa, el modelo ofrece una herramienta funcional para aproximarse al comportamiento del mercado en contextos de opacidad estadística. Los resultados confirman que el posicionamiento promocional y la exposición digital influyen de manera significativa en la probabilidad de adquisición.
Desde el punto de vista metodológico, el pipeline ETL reproducible y el uso de APIs públicas demuestran la viabilidad técnica y legal de construir sistemas de auditoría económica híbridos basados en minería de datos. Esta aproximación reduce el sesgo de sobreestimación presente en los registros fiscales aislados y permite una lectura territorial más precisa del ecosistema librero.
No obstante, el estudio reconoce limitaciones asociadas al sesgo de presencia digital, la exclusión de canales informales y las restricciones propias de la economía no observada. La omisión del comercio informal y de la piratería editorial implica que los resultados reflejan únicamente el segmento formal y parcialmente visible del mercado.

Referencias Bibliográficas 
	[43] Servicio Nacional de Derechos Intelectuales (SENADI), Informe de Operativos contra la Piratería Editorial, Quito, Ecuador, 2023.
	A. Booth et al., Systematic Approaches to a Successful Literature Review, Sage, 2016.
	Alm, J. et al. (2016). Moral tributaria e informalidad empresarial: Factores influyentes e impacto en la estrategia de negocio.
	Asamblea Nacional, "Ley Orgánica de Protección de Datos Personales," R.O. 459, 2021.
	B. Kitchenham, "Procedures for Performing Systematic Reviews," Keele Univ., Tech. Rep. TR/SE-0401, 2004.
	C. Wohlin, "Guidelines for Snowballing in Systematic Literature Reviews," EASE, 2014.
	Cámara Ecuatoriana del Libro, Estadísticas del Libro en Ecuador 2023–2024, Quito, Ecuador, 2024.
	CERLALC-UNESCO (2022). El ecosistema del libro en Iberoamérica, un estado de la cuestión. Bogotá, Colombia.
	CERLALC–UNESCO, El mercado editorial en América Latina: diagnóstico y tendencias, Bogotá, Colombia, 2020.
	Código Orgánico de la Economía Social de los Conocimientos, Creatividad e Innovación (COESCI), Registro Oficial del Ecuador, 2016.
	Código Orgánico Integral Penal (COIP), Art. 208, Registro Oficial del Ecuador, 2018.
	D. Moher et al., "The PRISMA statement," PLoS Med., vol. 6, no. 7, 2009.
	DBSCAN (Ester et al., 1996)
	E. Campaña, S. Pilca, M. Filian y J. Crespo, “Análisis Integral de la Piratería Editorial en el Ecuador (2020–2025): Metodologías de detección, cuantificación económica y marco regulatorio,” Revista Ingenio, Univ. Central del Ecuador, 2025.
	F. J. García-Peñalvo, "Revisión sistemática de literatura en Tesis Doctorales," Salamanca, 2017.
Geocoding API," 2024.
	Gobiernos Autónomos Descentralizados Provinciales del Ecuador, Planes de Desarrollo y Ordenamiento Territorial (PDOT) 2023–2027, Ecuador, 2023.
	Google Developers, "Books API Volume Reference," 2024.
	Google Developers, "Places API Documentation," 2024.
	Grupo. (2025). Análisis del Mercado de Librerías y Piratería Editorial en las Provincias de Bolívar y Santo Domingo, Ecuador. Revista Ingenio.
	Grupo10. (2025). Analysis Of The Supply And Distribution Of Editorial Products In The Provinces Of Sucumbíos And Napo, Ecuador: A Systematic Literature Review. Revista Ingenio.
	Grupo12. (2025). Bookstores In Pichincha And Pastaza. Revista Ingenio.
	Grupo2. (2025). Caracterización territorial del sector librero en Ecuador: un enfoque híbrido para la identificación de librerías y estimación cantonal de ventas en Tungurahua y Morona Santiago. Revista Ingenio.
	Grupo5. (2025). Intelligent System For The Analysis Of The Bookstore Ecosystem And Book Piracy At The Provincial Of Ríos And Orellana: Integration Of Sri Data, Multi-source Scraping And Analysis With Artificial Intelligence. Revista Ingenio.
	Grupo7. (2025). Geolocalización del ecosistema comercial-productivo del libro en Zamora Chinchipe e Imbabura y su relación con el comercio exterior del libro (2015–2025): SLR y estudio exploratorio. Revista Ingenio.
	IEEE Std 1028-2008, IEEE Standard for Software Reviews and Audits, 2008.
	INEC, "Directorio de Empresas y Establecimientos (DIEE)," 2023.
	Instituto Nacional de Estadística y Censos (INEC), Encuesta de Hábitos Lectores, Prácticas y Consumos Culturales, Quito, Ecuador, 2021.
	International Intellectual Property Alliance (IIPA), Copyright Protection and Enforcement: Ecuador, Washington, DC, USA, 2022.
	J. Cruz-Benito, "Analyzing software architectures through SLR," Telematics and Informatics, 2019.
	J. VanderPlas, Python Data Science Handbook, O'Reilly Media, 2016.
	K. Petersen et al., "Systematic mapping studies in software engineering," EASE, 2008.
	Leaflet.js, "Interactive Maps Documentation," 2024.
	M. J. Grant and A. Booth, "A typology of reviews," Health Inf. Libr. J., 2009.
	Montalvo Armas, G. (2019). Industria editorial en Ecuador—La Barra Espaciadora.
	OECD and UNESCO, Measuring the Cultural and Creative Economy, Paris, France, 2021
	OECD, Culture and Local Development: Maximising the Impact, Paris, France, 2018.
	OECD, Culture and Local Development: Maximising the Impact, Paris, France, 2018.
	OpenStreetMap, "Nominatim
	Organización Mundial de la Propiedad Intelectual (OMPI), Guía sobre Industrias Creativas y Desarrollo Económico, Ginebra, Suiza, 2022.
	P. Austin et al., "Using Google Places API for Economic Indicators," IMF Working Papers, 2021. M. Luca, "Reviews, Reputation, and Revenue," HBS Working Paper, 12-016, 2016.
	R. Mitchell, Web Scraping with Python, 2nd ed. O'Reilly Media, 2018.
	S. Brin and L. Page, "The anatomy of a large-scale Web search engine," Comp. Netw., 1998.
	Secretaría Nacional de Planificación (2024). Plan Nacional de Desarrollo 2024–2025. Gobierno del Ecuador.
	Secretaría Nacional de Planificación del Ecuador (SENPLADES), Plan Nacional de Desarrollo 2024–2025, Quito, Ecuador, 2024.
	Servicio de Rentas Internas del Ecuador, Directorio de Contribuyentes por Actividad Económica (CIIU G4761), Quito, Ecuador, 2024.
	SRI, "Catastro de Contribuyentes y Datos Abiertos," 2024.
	Superintendencia de Compañías, "Portal de Información Societaria," 2024.
	T. Dyba and T. Dingsøyr, "Empirical studies of agile software: A systematic review," IST, 2008.
	Throsby, D. (2008). The Economics of Cultural Policy. Cambridge University Press.
	U.S. Trade Representative (USTR), Special 301 Report on Copyright Protection and Enforcement, Washington, DC, USA, 2024.
	UNESCO, Global Education Monitoring Report: Cultural Access and Reading Ecosystems, Paris, France, 2022.
	UNESCO, Global Education Monitoring Report: Cultural Access and Reading Ecosystems, Paris, France, 2022.
	United Nations, Transforming our World: The 2030 Agenda for Sustainable Development, New York, NY, USA, 2015.
	V. L. Levenshtein, "Binary codes capable of correcting deletions," Soviet Physics Doklady, 1966.
	Vázquez, I. (2022). El libro y su industria en el marco de las industrias culturales. Modelizaciones económicas y características económico-sociales. Profesional de la información, v. 31, n. 2.
	W. McKinney, Python for Data Analysis, 2nd ed. O'Reilly Media, 2017.
	World Intellectual Property Organization (WIPO), The Economic Impact of Copyright-Based Industries, Geneva, Switzerland, 2021.
	World Intellectual Property Organization (WIPO), The Economic Impact of Copyright-Based Industries, Geneva, Switzerland, 2021.

