class Paciente:
    def __init__(self,nome,telefone,endereco,email,genero,nascimento):
        self.nome=nome
        self.telefone=telefone
        self.endereco=endereco
        self.email=email
        self.genero=genero
        self.nascimento=nascimento
    
    def is_old(nascimento):
        old=2023-nascimento
        return old
           
class is_old(Paciente):
    def __init__(self, nome, telefone, endereco, email, genero, nascimento):
        super().__init__(nome, telefone, endereco, email, genero, nascimento)
        old=2023-nascimento
        return old
            