# Exploración de las dinámicas entre suelo y aguas subterráneas en el Salar del Huasco

Este repositorio presenta una propuesta de análisis exploratorio de datos usando el lenguaje de programación Python. Los datos provienen de piezómetros y sensores de suelo instalados en una estación de monitoreo en el [Salar del Huasco](https://maps.app.goo.gl/5Z6byBViTpMrvNR28) en el altiplano de la Región de Tarapacá, Chile.

Este README describe los contenidos del repositorio. El análisis exploratorio está disponible en la [página web](https://pibonacic.github.io/salt-flats-groundwater-depth/). 

![Laguna](https://github.com/pibonacic/Huasco-salt-flat-groundwater-and-soil-dynamics/blob/main/figures/laguna.JPG)
Laguna del Salar del Huasco.

## Descripción del proyecto


## Objetivo
Explorar las relaciones entre profundidad del agua subterránea y variables medidas en el suelo a diferentes profundidades en una estación de monitoreo del Salar del Huasco.


## Audiencia
Este repositorio está dirigido a estudiantes, investigadores y profesionales con interés en:
- El estudio de la zona vadosa e hidrogeología en zonas áridas
- El uso de Python para la automatización de análisis y visualización de datos ambientales 


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
