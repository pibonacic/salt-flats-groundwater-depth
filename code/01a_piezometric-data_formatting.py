# IMPORTACIONES

import pandas as pd
import glob
import os


# DEFINICION DE VARIABLES AUXILIARES

# Diccionario con nombres de columna originales y nuevos
columns_dict = {
    'TEMPERATURE' : 'temperature_C',
    'NE_m' : 'depth_m',
    'Cota_m' : 'static_level_masl'
}

# Lista con nombres de columnas no necesarias
columns_list = [
    'ms',
    'LEVEL',
    'P_baro'
]


# DEFINCION DE FUNCIONES

# Funcion para la lectura y manejo de fechas
def configure_timestamps(file_path):
    """
    Lee un archivo xlsx, crea una columna Timestamps con formato datetime
    uniendo las columnas de fecha y hora y la establece como indice.
    """
    # Lee el archivo xlsx
    df_raw = pd.read_excel(file_path)

    # Convierte las columnas 'Date' y 'Time' en strings
    date_str = df_raw['Date'].astype(str)
    time_str = df_raw['Time'].astype(str)

    # Crea la columna 'Timestamps' con formato datetime a partir de 'Date' y 'Time'
    df_raw['Timestamps'] = pd.to_datetime(
        date_str + ' ' + time_str,
        format='%Y-%m-%d %H:%M:%S'
    )

    # Establece 'Timestamps' como indice
    df_raw = df_raw.set_index('Timestamps')

    # Elimina las columnas 'Date' y 'Time'
    df = df_raw.drop(columns=['Date', 'Time'])

    return df

# Funcion para el formateo de columnas
def format_columns(df):
    """
    Renombra y elimina columnas de un df a partir de un diccionario y lista respectivamente.
    Convierte las columnas restantes a tipo numerico.
    """
    # Renombra las columnas usando columns_dict y elimina aquellas en columns_list
    df_formatted = df.rename(
        columns=columns_dict).drop(
            columns=columns_list, axis=1, errors='ignore')
    
    # Itera sobre todas las columnas excepto Timestamps para convertirlas a tipo numerico
    for col in df_formatted.columns:
        if col != 'Timestamps':
            # errors='coerce' transforma cualquier valor no numerico en NaN
            df_formatted[col] = pd.to_numeric(df_formatted[col], errors='coerce')
    
    return df_formatted


# MANEJO DE RUTAS Y ARCHIVOS

# Ruta a la carpeta con los datos crudos
raw_data_path = '../data/raw/piezometers/'

# Patron en archivos crudos para buscar dentro de la carpeta
file_pattern = '*COMPENSADA.xlsx'

# Ruta a la carpeta de salida
output_path = '../data/processed/01_formatted'

# Crea la carpeta de salida en caso de que no exista
os.makedirs(output_path, exist_ok=True)

# Construye un patron de ruta usando el patron de file_pattern
filepath_pattern = os.path.join(raw_data_path, file_pattern)

# Genera una lista con las rutas de las archivos que cumplen con el patron
piezometer_files = glob.glob(filepath_pattern)

# Imprime los archivos crudos encontrados en la carpeta
if piezometer_files:
    print(f'{len(piezometer_files)} archivos identificados:')
    for filepath in sorted(piezometer_files):
        print(f'  - {filepath}')


## BUCLE DE EJECUCION

# Itera sobre el archivo de cada piezometro
for filepath in piezometer_files:

    # Extrae el nombre del archivo desde la ruta completa
    basename = os.path.basename(filepath)

    # Extrae el nombre del piezometro: penultima cadena de texto separada por '_'
    piezometer_name = basename.split('_')[-2].strip()
    print(f'Procesando piezometro {piezometer_name}')

    # Aplica la funcion configure_timestamps para leer el archivo y manejar las fechas
    df = configure_timestamps(filepath)
    print('  Indice timestamp configurado.')

    # Aplica la funcion format_columns
    df_formatted = format_columns(df)
    print('  Nombres de columnas formateados.')

    # Construye el nombre de salida del archivo
    output_filename = f'piezo-data_{piezometer_name}_formatted.csv'

    # Construye la ruta de salida del archivo
    output_filepath = os.path.join(output_path, output_filename)

    # Exporta el archivo como csv
    df_formatted.to_csv(output_filepath)
    print(f'  Datos procesados guardados en: {output_filepath}\n')