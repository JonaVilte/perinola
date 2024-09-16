

class Fichas:
    def __init__(self):
        self.ficha = 0
    
    def __repr__(self):
        return f"Apuesta: {self.ficha} fichas"
    
    def ponerFichas(self, cuantas=1):
        self.ficha = self.ficha + cuantas

    def tomarFicha(self, cuantas=1):
        if cuantas > self.ficha:
            raise ValueError(f"No hay tantas fichas (no se pueden sacar {cuantas} quedan {self.ficha})")
        self.ficha = self.ficha - cuantas

    def tomarTodas(self):
        if self.ficha == 0:
            raise ValueError("No se puede tomar fichas")
        self.total = self.ficha - self.ficha 
         
        return f"Tengo {self.ficha} fichas y quedan {self.total} fichas en la mesa"
    
    def tieneFicha(self, cuantas=1):
        if cuantas == self.ficha:
            return True
    def estaVacia(self):
        if self.total == 0:
            return True


