# Exploración de las dinámicas entre suelo y aguas subterráneas en el Salar del Huasco

Este repositorio presenta un análisis exploratorio a partir de datos piezométricos y de suelos registrados en el [Salar del Huasco](https://maps.app.goo.gl/5Z6byBViTpMrvNR28), en el altiplano de la Región de Tarapacá, Chile. 

PYTHON

Este README describe el repositorio; el análisis exploratorio se presenta en esta [página web](https://pibonacic.github.io/salt-flats-groundwater-depth/). 

## Contenidos

-  [Descripción del proyecto]
-  [Estructura del repositorio]
-  [Flujo de trabajo]
-  [Descripción de los scripts]
-  


## Descripción del proyecto


## Objetivo
Explorar las relaciones entre profundidad del agua subterránea y variables medidas en el suelo (contenido de agua y temperatura), usando el Salar del Huasco como caso de estudio.


## Audiencia
Este repositorio está dirigido a estudiantes, investigadores y profesionales con interés en:
- El estudio de la zona vadosa e hidrogeología en zonas áridas
- El uso de Python para el análisis y visualización de datos ambientales 


## Estructura del repositorio

``` text
Huasco-salt-flat-groundwater-and-soil-dynamics/
├── README.md
├── code
├── data/
│   ├── raw/
│   │   ├── piezometers/
│   │   └── soil-sensors/
│   └── processed/
│       ├── 01_formatted
│       ├── 02_cleaned
│       └── 03_daily
├── docs/
├── figures/
└── quarto-website/
```


## Flujo de trabajo
01. Lectura y formateo de datos crudos
02. Identificación y remoción de outliers
03. Agregación diaria
04. Visualización


## Descripción de los códigos

-  `01a_piezometric-data_formatting.py`\
    Lee uno o más archivos .xlsx y renombra sus columnas. Acepta un archivo por piezómetro. Produce un .csv por piezómetro.
   
-  `01b_soil-data_formatting.py`\
    Lee uno o más archivos .csv y renombra sus columnas. Acepta múltiples archivos por datalogger. Produce un .csv por datalogger.

-  `02a_piezometric-data_cleaning.py`\
    Lee uno o más archivos .csv, identifica valores anómalos circunscritos a campañas de terreno y los remueve. Produce un .csv por piezómetro.
    
-  `03_all-data_daily-aggregation.py`\
    Lee uno o más archivos .csv y agrega los datos calculando el promedio diario. Produce un .csv por archivo de entrada.
  
-  `04_all-data_exploratory-visualization.ipynb`\
    Lee uno o más archivos .csv, transforma los datos y genera cinco visualizaciones.\
    Archivo tipo notebook: los procesamientos están estructurados en celdas de código.

## Agradecimientos
Esta investigación es financiada por la Agencia Nacional de Investigación y Desarrollo de Chile (ANID), mediante los proyectos ATE/230006 y FONDECYT/1251067.
El autor agradece a la Asociación Indígena Aymara Laguna del Huasco y a la Corporación Nacional Forestal (CONAF) por permitir el levantamiento de datos en el Salar del Huasco.

## Declaración de uso de inteligencia artificial generativa
Durante el desarrollo de este trabajo, el autor utilizó Google Gemini para escribir y revisar código de programación. Después de usar la herramienta, el autor revisó críticamente y editó el contenido según fue necesario, y asume plena responsabilidad por la información presentada.
