class Cliente:
    def __init__(self,nome:str,email:str,cpf:str,senha:str):
        self.nome=nome
        self.email=email
        self.cpf=cpf
        self.senha=senha
        
    def banco_dados(self,lista_cliente):
        lista_cliente=[]
        lista_cliente.append(self.nome,self.email,self.cpf,self.senha)
        return lista_cliente
    
    def escolher_plano(self,plano:str,erro:str):
        self.plano=plano
        self.lista_plano=['basic','premium']
        if self.plano in self.lista_plano:
            return plano
        else:
            erro=('PLANO ESCOLHIDO INVALIDO')
            return erro
        
    def mudar_plano(self,novo_plano:str):
        if novo_plano in self.lista_plano:
            self.plano=novo_plano
            return novo_plano
            
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

        
        