from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

from schemas import ComentarioSchema


class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "Pedro Brum Vieira"
    cpf: Optional[int] = 11209074621
    celular: int = 32999127280


class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cliente.
    """
    nome: str = "Teste"


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    clientes:List[ClienteSchema]


def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "celular": cliente.celular,
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: cliente + comentários.
    """
    id: int = 1
    nome: str = "Pedro Brum Vieira"
    cpf: Optional[int] = 11209074621
    celular: int = 32999127280
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "cpf": cliente.cpf,
        "celular": cliente.celular,
        "total_cometarios": len(cliente.comentarios),
        "comentarios": [{"texto": c.texto} for c in cliente.comentarios]
    }
