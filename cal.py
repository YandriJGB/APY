import requests  # Para hacer peticiones HTTP
from dotenv import load_dotenv  # Para cargar variables desde el archivo .env
import os  # Para acceder a las variables de entorno del sistema

# Cargar las variables del archivo .env
load_dotenv()

# Obtener clave de API y motor de búsqueda desde las variables de entorno
API_KEY = os.getenv("API_KEY_SEARCH_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

# Consulta que se quiere buscar
query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
# Query pide los datos en cierto formato, aquí archivos SQL con nombre exacto "MySQL dump" porque está entre comillas
# Lo último (pass|password|passwd|pwd) son palabras clave relacionadas con contraseñas

lang = "lang_es"
# lang = idioma, en este caso idioma español

# Función que construye la URL para hacer la búsqueda usando la API de Google
def Busqueda(query, page, lang, API_KEY, SEARCH_ENGINE_ID):
  return f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}&lr={lang}"

# Función que hace la petición a la API y devuelve los datos en formato JSON
def Resultado(url):
  response = requests.get(url)
  return response.json()

# Función que muestra los resultados encontrados
def Res(results):
  # Si no hay resultados, mostrar mensaje
  if not results:
    print("No se encontraron resultados.")
  else:
    # Si hay resultados, mostrar título, enlace y descripción
    for item in results:
      title = item.get('title')
      link = item.get('link')
      snippet = item.get('snippet')

      print(f"Title: {title}")
      print(f"Link: {link}")
      print(f"Snippet: {snippet}")
      print("-" * 80)

# Función principal que organiza la ejecución
def main():
  page = 1  # Página de inicio (puede modificarse para paginar)
  url = Busqueda(query, page, lang, API_KEY, SEARCH_ENGINE_ID)  # Construir la URL
  data = Resultado(url)  # Hacer la petición
  results = data.get('items', [])  # Obtener los resultados
  Res(results)  # Mostrar los resultados

# Ejecutar el programa
if __name__ == "__main__":
  main()

