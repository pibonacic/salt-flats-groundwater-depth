# Exploración de las dinámicas entre suelo y aguas subterráneas en el Salar del Huasco

Este repositorio presenta una propuesta de análisis exploratorio de datos piezométricos y edáficos usando el lenguaje de programación Python. El área de estudio es el [Salar del Huasco](https://maps.app.goo.gl/5Z6byBViTpMrvNR28), ubicado en el altiplano de la Región de Tarapacá, Chile. Este README describe los contenidos del repositorio. El análisis exploratorio está disponible en la [página web](https://pibonacic.github.io/Huasco-salt-flat-groundwater-and-soil-dynamics/). 

![Laguna](https://github.com/pibonacic/Huasco-salt-flat-groundwater-and-soil-dynamics/blob/main/figures/laguna.JPG)
Laguna del Salar del Huasco.

## Objetivo
Explorar las relaciones entre profundidad del agua subterránea y variables medidas en el suelo, usando el Salar del Huasco como caso de estudio.


## Audiencia
Este repositorio está dirigido a estudiantes, investigadores y profesionales con interés en:
- El estudio de la zona vadosa e hidrogeología en zonas áridas
- El uso de Python para la automatización de análisis y visualización de datos ambientales
- El análisis estadístico de series temporales de datos ambientales


## Estructura del repositorio
El repositorio cuenta con dos carpetas principales: _code_ y _data_, que en conjunto tienen todos los archivos necesarios para reproducir el análisis exploratorio. Las carpetas _docs_, _figures_ y _quarto-website_ se utilizan para elaborar la página web con los resultados del análisis.

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

### Código
Cada _script_ fue desarrollado con un objetivo particular y para ser ejecutado secuencialmente. El flujo de trabajo diseñado fue el siguiente:

``` text
01. Lectura y formateo de datos crudos
02. Identificación y remoción de outliers
03. Agregación diaria
04. Visualización
```

El nombre de cada _script_ indica su posición en el flujo de trabajo, el tipo de dato que procesa y su función, siguiendo la estructura numero_tipo-dato_funcion. A continuación, se describe brevemente cada uno:

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


### Datos
Los datos provienen de un piezómetro y tres sensores de suelo instalados a diferentes profundidades (15, 30 y 48 cm) en una estación de monitoreo del salar del Huasco. Los registros disponibles abarcan desde mayo de 2024 hasta julio de 2025. Los datos crudos se encuentran en la subcarpeta _raw_ y aquellos generados por los _scripts_ en la subcarpeta _processed_.


## Agradecimientos
Esta investigación es financiada por la Agencia Nacional de Investigación y Desarrollo de Chile (ANID), mediante los proyectos ATE/230006 y FONDECYT/1251067.
El autor agradece a la Asociación Indígena Aymara Laguna del Huasco y a la Corporación Nacional Forestal (CONAF) por permitir el levantamiento de datos en el Salar del Huasco.

Se extiende un agradecimiento especial a los miembros del equipo [Altiplano Wetlands](https://altiplanowetlands.cl) que con gran esfuerzo están empujando la investigación en humedales altoandinos.


## Declaración de uso de inteligencia artificial generativa
Durante el desarrollo de este trabajo, el autor utilizó Google Gemini para escribir y revisar código de programación. El autor revisó críticamente y editó el contenido generado según fue necesario, y asume plena responsabilidad por la información presentada.
