import requests
import time

API_URL = "https://rickandmortyapi.com/api/character"

def fetch_all_characters():
    start_time = time.time() 
    alive_characters = []
    dead_characters = []
    page = 1

    while True:
        response = requests.get(f"{API_URL}?page={page}")
        elapsed_time = time.time() - start_time
        status_code = response.status_code

        if status_code != 200:
            print(f"Error: Código de estado {status_code}")
            break

        data = response.json()
        if not isinstance(data, dict) or "results" not in data:
            print("Error: Formato inesperado de la respuesta")
            break

        characters = data["results"]

        for char in characters:
            if not isinstance(char["name"], str) or not isinstance(char["status"], str):
                print(f"Error en tipos de datos en: {char}")
                continue

            if char["status"].lower() == "alive":
                alive_characters.append(char)
            elif char["status"].lower() == "dead":
                dead_characters.append(char)

        if data["info"]["next"]:
            page += 1
        else:
            break

    print(f"Tiempo de respuesta: {elapsed_time:.2f} segundos")
    print(f"Código de estado: {status_code}")
    print(f"Total de personajes vivos encontrados: {len(alive_characters)}")
    print(f"Total de personajes muertos encontrados: {len(dead_characters)}")

    
    print("\nPrimeros 5 personajes vivos:")
    for char in alive_characters[:5]:
        print(f"{char['name']} - {char['status']}")

    print("\nPrimeros 5 personajes muertos:")
    for char in dead_characters[:5]:
        print(f"{char['name']} - {char['status']}")

if __name__ == "__main__":
    fetch_all_characters()