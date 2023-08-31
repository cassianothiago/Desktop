class Saldo:
    def depositar(self,num1:int,num2:int):
        saldo=num1+num2
        self.__saldof(saldo)
    
    def sacar(self,num1:int,num2:int):
        saldo=num1-num2
        self.__saldof(saldo)
        
    def __saldof(self,saldo:int):
        self.__saldo=saldo
        return (self.__saldo) 