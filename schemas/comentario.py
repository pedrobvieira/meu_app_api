from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    cliente_id: int = 1
    texto: str = "Seja bem-vindo!"
