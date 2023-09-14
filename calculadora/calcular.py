class Calculo:       
    def calcular(self,expresao:str):
        self.expresao=expresao
        self.resultado=eval(self.expresao)
        print(self.resultado)
        
        
    
calc=Calculo()
calc.calcular('10/8')

        
    