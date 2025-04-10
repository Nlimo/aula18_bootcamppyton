from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contratao de Dados/ Schema de Dados/ View da minha API
    name: str
    type: str
    
    class Config:
        from_attributes = True
