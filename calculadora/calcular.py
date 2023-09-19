class Calculo:       
    def calcular(self,expresao:str):
        self.expresao=expresao
        self.resultado=eval(self.expresao)
        return self.resultado
        
        

    

        
    