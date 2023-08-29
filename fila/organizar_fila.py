class Paciente:
    def __init__(self,nome:str,telefone:int,email:str,genero:str,ano_nascimento:str):
        self.nome=nome
        self.telefone=telefone
        self.email=email
        self.genero=genero
        self.ano_nascimento=ano_nascimento
    
class Is_old(Paciente):
    def __init__(self, nome: str, telefone: int, email: str, genero: str, ano_nascimento: str):
        super().__init__(nome, telefone, email, genero, ano_nascimento)
        
    def is_old(self):
        old=2023-self.ano_nascimento
        if old>60:
            lista=[]
            lista.append(old,self.nome,self.telefone,self.email)
        
        