from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    cpf = Column(Integer)
    celular = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o cliente e o comentário.
    # Essa relação é implicita, não está salva na tabela 'cliente',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, cpf:int, celular:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            nome: nome do cliente.
            cpf: cpf do cliente
            celular: celular do cliente
            data_insercao: data de quando o cliente foi inserido à base
        """
        self.nome = nome
        self.cpf = cpf
        self.celular = celular

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Cliente
        """
        self.comentarios.append(comentario)

