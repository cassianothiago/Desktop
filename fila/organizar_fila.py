class Paciente:
    def __init__(self,nome:str,telefone:int,email:str,genero:str,ano_nascimento:int):
        self.nome=nome
        self.telefone=telefone
        self.email=email
        self.genero=genero
        self.ano_nascimento=ano_nascimento
        
    def is_old(self,nascimento):
        old=2023-nascimento
        if old>=60:
            print('Paciente idoso')
    
    def is_pcd(self,pcd:str):
        self.pcd=pcd
        if pcd=='sim':
            print('Paciente PCD')


nome=input('nome = ')
tel=int(input('telefone = '))
email=input('email = ')
genero=input('genero = ')
ano_nascimento=int(input('ano nascimento = '))

paciente=Paciente(nome,tel,email,genero,ano_nascimento)
pcd=input('é pcd(sim ou nao) = ')
paciente.is_old(ano_nascimento)
paciente.is_pcd(pcd)
lista=[]
lista.append(nome)
lista.append(tel)
lista.append(email)
lista.append(genero)
lista.append(ano_nascimento)
print(lista)

    
            
        
        