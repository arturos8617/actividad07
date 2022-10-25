from particulasact.algoritmos import distancia_euclidiana


class Particula:
    def __init__(self, id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue, distancia=None):
        if distancia:
            self.creadorParticulas(id, origen_x, origen_y, destino_x,
                                   destino_y, velocidad, red, green, blue, distancia)

        else:
            self.distancia = distancia_euclidiana(
                origen_x, origen_y, destino_x, destino_y)
            self.creadorParticulas(id, origen_x, origen_y, destino_x,
                                   destino_y, velocidad, red, green, blue, self.distancia)

    def creadorParticulas(self, id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue, distancia):
        self.id = id
        self.origen_x = origen_x
        self.origen_y = origen_y
        self.destino_x = destino_x
        self.destino_y = destino_y
        self.velocidad = velocidad
        self.red = red
        self.green = green
        self.blue = blue
        self.distancia = distancia

    def __str__(self):
        return f"Id: {self.id}\nOrigen X: {self.origen_x}\nOrigen Y: {self.origen_y}\nDestino X: {self.destino_x}\nDestino Y: {self.destino_y}\nVelocidad: {self.velocidad}\nRed: {self.red}\nGreen: {self.green}\nBlue: {self.blue}\nDistancia: {self.distancia}\n\n"

    def to_dict(self):
        return {
            "id": self.id,
            "origen_x": self.origen_x,
            "origen_y": self.origen_y,
            "destino_x": self.destino_x,
            "destino_y": self.destino_y,
            "velocidad": self.velocidad,
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
            "distancia": self.distancia
        }
