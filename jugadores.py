class Jugador:
    def __init__(self, nombre, ficha=5 ):
        self.nombre = nombre
        self.ficha = ficha 

    def __repr__(self):
        return f"{self.nombre}, {self.ficha} fichas"
    
    def darFicha(self, cuantas = 1):
        self.ficha += cuantas

    def sacarFicha(self, cuantas = 1):
        if cuantas > self.ficha:
            raise ValueError(f"No se puede sacar mas fichas de las que tiene el jugador")
        self.ficha -= cuantas

    def tieneFicha(self, cuantas=1):
        return cuantas >= self.ficha
        
        
    def sinFichas(self):
        return self.ficha <= 0
            

