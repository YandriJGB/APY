import os
import requests
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Fetch API key and search engine ID from environment variables
API_KEY = os.getenv("API_KEY_SEARCH_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

# Constants for the search query and parameters
QUERY = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
LANGUAGE = "lang_es"


def build_search_url(query: str, page: int, lang: str) -> str:
    """Build the URL for the Google Custom Search API."""
    return f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}&lr={lang}"


def get_search_results(url: str) -> list:
    """Fetch the search results from the Google Custom Search API."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any failed request
    data = response.json()
    return data.get('items', [])


def display_results(results: list) -> None:
    """Display the search results in a readable format."""
    if not results:
        print("No se encontraron resultados.")
        return

    for item in results:
        title = item.get('title', 'No Title')
        link = item.get('link', 'No Link')
        snippet = item.get('snippet', 'No Snippet')
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Snippet: {snippet}")
        print("-" * 80)


def main():
    """Main function to execute the search and display results."""
    search_url = build_search_url(QUERY, page=1, lang=LANGUAGE)
    search_results = get_search_results(search_url)
    display_results(search_results)


if __name__ == "__main__":
    main()
