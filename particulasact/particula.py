from particulasact.algoritmos import distancia_euclidiana


class Particula:
    def __init__(self, id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue):
        self.id = id
        self.origen_x = origen_x
        self.origen_y = origen_y
        self.destino_x = destino_x
        self.destino_y = destino_y
        self.velocidad = velocidad
        self.red = red
        self.green = green
        self.blue = blue
        self.distancia = distancia_euclidiana(
            origen_x, origen_y, destino_x, destino_y)

    def __str__(self):
        return f"Id: {self.id}\nOrigen X: {self.origen_x}\nOrigen Y: {self.origen_y}\nDestino X: {self.destino_x}\nDestino Y: {self.destino_y}\nVelocidad: {self.velocidad}\nRed: {self.red}\nGreen: {self.green}\nBlue: {self.blue}\nDistancia: {self.distancia}\n\n"
