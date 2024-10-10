from sqlalchemy import Column, String, BIGINT, REAL
from src.models.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):

    __tablename__ = 'Pessoa Juírica'
    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable= False)
    idade = Column(BIGINT, nullable= False)
    nome_fantasia = Column(String, nullable= False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"Pessoa Jurídica [nome_fantasia={self.nome_fantasia}, faturamento={self.faturamento}, saldo={self.saldo}]"
