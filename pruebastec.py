"""
import requests
import pandas as pd
from openpyxl import load_workbook

# URL del enlace que contiene la información que deseas descargar
url = "https://sinergox.xm.com.co/anamul/_layouts/15/WopiFrame2.aspx?sourcedoc={DE1DA2B0-02AD-4DB5-895C-889FC94683B6}&file=CONSUMOS%20FRONTERAS.xlsx&action=default"
# Contraseña del archivo Excel
user="ISAMDNT\1014244632"
password = "C0L0mb14202155"

# Realiza la solicitud HTTP para obtener los datos
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea los datos a un DataFrame de pandas
    df = pd.read_html(response.text)[0]  # Ajusta el índice [0] según la estructura de la página web

    # Guarda el DataFrame en un archivo Excel
    with pd.ExcelWriter("informacion_descargada.xlsx", engine='openpyxl') as writer:
        writer.book = load_workbook("informacion_descargada.xlsx")
        df.to_excel(writer, sheet_name="Hoja1", index=False)

    # Establece la contraseña para el archivo Excel
    writer.book.security.set_password(password)
    writer.book.security.set_user(user)

    print("Información descargada y guardada en 'informacion_descargada.xlsx' con contraseña.")
else:
    print("No se pudo acceder al enlace. Código de estado:", response.status_code)
"""

#se debe instalar en consola para que funcione: pip install requests pandas requests_ntlm

import requests
import pandas as pd
from requests_ntlm import HttpNtlmAuth

# URL del enlace que contiene la información que deseas descargar
url = "https://sinergox.xm.com.co/anamul/_layouts/15/WopiFrame2.aspx?sourcedoc={DE1DA2B0-02AD-4DB5-895C-889FC94683B6}&file=CONSUMOS%20FRONTERAS.xlsx&action=default"

# Credenciales de acceso
username = "ISAMDNT\1014244632"
password = "C0L0mb14202155"

# Realiza la solicitud HTTP con autenticación NTLM
response = requests.get(url, auth=HttpNtlmAuth(username, password))

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Descarga el archivo Excel
    with open("informacion_descargada.xlsx", "wb") as output_file:
        output_file.write(response.content)

    print("Información descargada y guardada en 'informacion_descargada.xlsx'.")
else:
    print("No se pudo acceder al enlace. Código de estado:", response.status_code)
