###################################################
#              Generador de leads                 #
# V.1.0.0 //14 12 2025//                          #
# V.1.0.1 //16 12 2025//                          #
# V.1.2.4 //28 12 2025//                          #
# V.1.3.7 //07 01 2026//                          #
# V.1.3.10 //16 01 2026//                         #
# Desarrollado con Gemini Flash Preview           #
# Desplegado con streamlit                        #
# Desarrollador: Sergio Emiliano López Bautista   #
###################################################


# ------------------------- Requerimientos y librerías -------------------------------
import os
from time import time
from dotenv import load_dotenv
from google import genai

# -------------------------------- Estructuras ---------------------------------------
inicio = time()
# --------------------------------- Seteadores ---------------------------------------
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

inter = time()
print(f"Tiempo de carga de librerías: {inter - inicio} segundos")

# ---------------------------------- Funciones ---------------------------------------

# ------------------------------------ MAIN ------------------------------------------

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Hola"
)   

print(response.text)

fin = time()
print(f"Tiempo de ejecución: {fin - inicio} segundos")