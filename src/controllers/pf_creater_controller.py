from typing import Dict
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from .interfaces.pf_creater_controller import PFCreaterControllerInterface

class PFCreaterController(PFCreaterControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        
    def create(self, people_info: Dict) -> Dict:
        renda_mensal = people_info["renda_mensal"]
        idade = people_info["idade"]
        nome_completo = people_info['nome_completo']
        celular = people_info["celular"]
        email = people_info['email']
        categoria = people_info['categoria']
        saldo = people_info["saldo"]

        self.__insert_person_in_db(renda_mensal, idade, nome_completo, 
                                   celular, email, categoria, saldo)
        formated_response = self.__format_response(people_info)

        return formated_response

    def __insert_person_in_db(self, renda_mensal: int, idade: int, nome_completo: str, celular: str,
                              email: str, categoria: str, saldo: int) -> None:
        self.__pessoa_fisica_repository.insert_person(renda_mensal, idade, nome_completo, celular, 
                                                      email, categoria, saldo)
        
    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Pessoa Física",
                "count": 1,
                "attributes": person_info
            }
        }
