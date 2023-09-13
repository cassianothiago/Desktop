class Cliente:
    def __init__(self,nome:str,email:str,cpf:str,senha:str):
        self.nome=nome
        self.email=email
        self.cpf=cpf
        self.senha=senha
    
    def escolher_plano(self,plano:str):
        lista_plano=['basic','premium']
        if self.plano in lista_plano:
             return self.plano
        else: 
            self.plano = 'Plano inexistente'
            return self.plano
        
    def mudar_plano(self,novo_plano:str):
        lista_plano=['basic','premium']
        if novo_plano in lista_plano:
            return novo_plano
        else:
            novo_plano=str('Plano inexistente')
            return novo_plano
            
nome=input('digite seu nome: ')
email=input('digite seu email: ')
cpf=input('digite seu cpf: ')
senha=input('digite sua senha: ')
cliente=Cliente(nome,email,cpf,senha)
seu_plano=input('digite seu plano: ')
cliente.escolher_plano(seu_plano)
print(nome)
print(email)
print(cpf)
print(seu_plano)
