class Cliente:
    def __init__(self,nome,email,cpf,senha):
        self.nome=nome
        self.email=email
        self.cpf=cpf
        self.senha=senha

    def escolher_plano(self,plano,erro):
        lista_plano=['basic','premium']
        if plano in lista_plano:
            return plano
        else:
            erro=('PLANO ESCOLHIDO INVALIDO')
            return erro
            
'''nome=input('digite seu nome: ')
email=input('digite seu email: ')
cpf=input('digite seu cpf: ')
senha=input('digite sua senha: ')
cliente=Cliente(nome,email,cpf,senha)
print(nome)
print(email)
print(cpf)


plano=input('digite seu plano(basic ou premium): ')
cliente.escolher_plano(plano)'''

        
        