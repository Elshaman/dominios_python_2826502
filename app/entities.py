class Carro():

    def __init__(self, placa, tipo_vehiculo):
        self.placa = placa
        self.tipo_vehiculo = tipo_vehiculo

class Cliente():
    
    def __init__(self, 
                  nombre, 
                  celular, 
                  identificacion ,
                  lista_carros):
    
        self.nombre = nombre
        self.celular =celular
        self.identificacion = identificacion
        self.lista_carros = lista_carros

    def addCar(self, car):
        self.lista_carros.append = car

    def listCar(self):
        for carro in self.lista_carros:
            print(carro.nombre, 
                  carro.celular, 
                  carro.identificacion)
