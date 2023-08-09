from shape import*

class Retangulo(Shape):
    def __init__(self, cor, base, altura):
        super().__init__(cor)
        self.base=base
        self.altura=altura
        
        def calculo(self,base,altura):
            self.area=self.base*self.altura
            return self.area
            
            
        