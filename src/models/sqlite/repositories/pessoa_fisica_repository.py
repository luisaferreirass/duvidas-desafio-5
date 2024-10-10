from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface

class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_people(self) -> List[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                people = database.session.query(PessoaFisicaTable).all()
                return people
            except NoResultFound:
                return []
            
    def insert_person(self, renda_mensal: int, idade: int, nome_completo: str, 
                      celular: str, email: str, categoria: str, saldo: int):
        with self.__db_connection as database:
            try:
                person = PessoaFisicaTable(
                    renda_mensal= renda_mensal, 
                    idade= idade, 
                    nome_completo= nome_completo, 
                    celular= celular,
                    email= email, 
                    categoria= categoria, 
                    saldo= saldo)

                database.session.add(person)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def sacar(self, nome_completo: str, quantia: int):
        with self.__db_connection as database:
            try:
                person = (database.session
                          .query(PessoaFisicaTable)
                          .filter(PessoaFisicaTable.nome_completo == nome_completo)
                          .one())
                
                new_saldo = person.saldo - quantia

                new_person = PessoaFisicaTable(
                    renda_mensal= person.renda_mensal, 
                    idade= person.idade, 
                    nome_completo= person.nome_completo, 
                    celular= person.celular,
                    email= person.email, 
                    categoria= person.categoria, 
                    saldo= new_saldo)
                
                (database.session
                 .query(PessoaFisicaTable)
                 .filter(PessoaFisicaTable.nome_completo == nome_completo)
                 .delete())
                
                database.session.commit()
                database.session.add(new_person)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

            
                


        
