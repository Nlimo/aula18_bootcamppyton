import requests
from db import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchema

Base.metadata.create_all(bind=engine)

def pegar_pokemon(id: int) -> PokemonSchema:
    
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    if response.status_code == 200:
        data = response.json()
        data_types = data['types'] # Assumindo que 'data' é o dic com os dados
        types_list = []

        for type_info in data_types:
            types_list.append(type_info['type']['name'])
        types = ', '.join(types_list)
        return PokemonSchema(name = data['name'], type = types)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
    return db_pokemon