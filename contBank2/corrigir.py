class Cadastro:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if type(nome) == str and isinstance(idade,int):
            print('Banco de Dados')
            print(f'Usuario {nome}, com idade {idade} cadastrado')
        else:
            print('Dados Invalidos')

cads=Cadastro()
cads.cadastrar('thiago',10)

class Cadastrar:
    def __init__(self,nome: str,idade: int) -> None:
        