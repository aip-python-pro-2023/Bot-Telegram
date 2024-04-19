from pokeapi import PokeAPI


ditto = PokeAPI.get_pokemon("ditto")
print(ditto)


pokemon_generator = PokeAPI.get_all(get_full=True)
heaviest_pokemon = None
heaviest_weight = 0.0

for pokemon in pokemon_generator:
    print(pokemon)
    if hasattr(pokemon, "_weight") and pokemon._weight > heaviest_weight:
        heaviest_pokemon = pokemon
        heaviest_weight = pokemon._weight

print(f"Самый тяжелый из 50 Покемонов это: {heaviest_pokemon}")
