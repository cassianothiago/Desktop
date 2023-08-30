class Carro:
    def __init__(self,modelo: str, marca:str):
        self.modelo=modelo
        self.marca=marca
        
    def acelarar(self):
        print('acelerar')
    
    def freiar(self):
        print('freiar')
        
    def passar_marcha(self,marcha:int):
        print('o carro está na {}ª marcha'.format(marcha))
    
modelo=input('modelo = ')
marca=input('marca= ')
carro = Carro(modelo,marca)
print(carro.modelo)
print(carro.marca)
carro.acelarar()
carro.freiar()
marcha=int(input('qual marcha = '))
carro.passar_marcha(marcha)

    