import requests
from typing import Generator
from pokemon import Pokemon, BasePokemon

class PokeAPI:
    @staticmethod
    def get_pokemon(name_or_id: str) -> Pokemon:
        url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_id = data['id']
            name = data['name']
            height = data['height'] / 10  
            weight = data['weight'] / 10  
            return Pokemon(id=pokemon_id, name=name, height=height, weight=weight)
        else:
            raise Exception(f"Failed to get Pokemon with name or ID '{name_or_id}'")

    @staticmethod
    def get_all(get_full: bool = False) -> Generator[Pokemon, None, None]:
        url = "https://pokeapi.co/api/v2/pokemon?limit=50"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for pokemon_data in data['results']:
                name = pokemon_data['name']
                if get_full:
                    pokemon = PokeAPI.get_pokemon(name)
                else:
                    pokemon = BasePokemon(name=name)
                yield pokemon
        else:
            raise Exception("Failed to get list of Pokemon")
