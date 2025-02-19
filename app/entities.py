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


class Cupo():

    def __init__(self, letra):
        self.letra = letra

class Pago():

    def __init__(self,  
                 fecha_inicio, 
                 hora_inicio,
                 fecha_fin, 
                 hora_fin, 
                 valor,
                 carro,
                 cupo,
                 empleado):
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.fecha_fin = fecha_fin
        self.hora_fin = hora_fin
        self.valor = valor
        self.carro = carro
        self.cupo = cupo
        self.empleado = empleado


