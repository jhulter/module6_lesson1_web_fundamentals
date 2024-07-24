import requests
import json

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def fetch_pokemon_data(pokemon_name):
    url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    response = requests.get(url)
    json_data = response.text
    poke_data = json.loads(json_data)
    print(poke_data["name"])
    return poke_data

def calculate_average_weight():
    total_weight = 0
    for pokemon in pokemon_names:
        poke_data = fetch_pokemon_data(pokemon)
        total_weight += poke_data["weight"]
    return total_weight/len(pokemon_names)

for pokemon in pokemon_names:
    fetch_pokemon_data(pokemon)
print(calculate_average_weight())
