import pandas as pd

# Ruta del archivo Excel a importar
ruta_importar = r"C:\ProgramData\MyBots\002 - Envio Correos\Input\Base de datos correos.xlsx"

# Importar el archivo Excel
df = pd.read_excel(ruta_importar)

# Eliminar los datos duplicados de la columna "EMAIL COMERCIAL 1"
df_sin_duplicados = df.drop_duplicates(subset='EMAIL COMERCIAL 1')

# Ruta del archivo Excel a exportar
ruta_exportar = r"C:\ProgramData\MyBots\002 - Envio Correos\Input\Base de datos correos.xlsx"

# Exportar el DataFrame resultante a un nuevo archivo Excel
df_sin_duplicados.to_excel(ruta_exportar, index=False)
