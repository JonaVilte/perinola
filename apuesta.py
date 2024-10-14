class Apuesta:
    def __init__(self):
        self.ficha = 0
    
    def __repr__(self):
        return f"Apuesta: {self.ficha} fichas"
    
    def ponerFichas(self, cuantas=1):
        if cuantas < 1:
            raise ValueError("La cantidad de fichas a poner debe ser al menos 1")
        self.ficha += cuantas

    def tomarFicha(self, cuantas=1):
        if cuantas > self.ficha:
            raise ValueError(f"No hay tantas fichas (no se pueden sacar {cuantas} quedan {self.ficha})")
        self.ficha -= cuantas

    def tomarTodas(self):
        if self.ficha == 0:
            raise ValueError("No se puede tomar fichas")

        fichas = self.ficha
        self.ficha = 0          
        return fichas
    
    def tieneFicha(self, cuantas=1):
        return self.ficha >= cuantas 
            
    def estaVacia(self):
        return self.ficha == 0
            


