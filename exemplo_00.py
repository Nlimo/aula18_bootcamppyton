import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contratao de Dados/ Schema de Dados/ View da minha API
    name: str
    type: str
    
    class Config:
        from_attributes = True

def pegar_pokemon(id: int) -> PokemonSchema:
    
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data['types'] # Assumindo que 'data' é o dic com os dados
    types_list = []

    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name = data['name'], type = types)

if __name__ == "__main__":
    print(pegar_pokemon(25))
    print(pegar_pokemon(14))
    print(pegar_pokemon(7))