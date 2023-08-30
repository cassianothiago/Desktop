class Calculadora:
    def calcular(self,op):
        if op =='+':
            self.__adicionar()
        
        if op =='-':
            self.__subtrair()
            
    def __adicionar(self):
        numero1=int(input('1º numero = '))
        numero2=int(input('2º numero = '))
        print(numero1+numero2)
    
    def __subtrair(self):
        numero1=int(input('1º numero = '))
        numero2=int(input('2º numero = '))
        print(numero1-numero2)

calc=Calculadora()
calc.calcular('+')
calc.calcular('-')
