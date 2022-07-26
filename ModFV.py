from http.client import PROXY_AUTHENTICATION_REQUIRED


class panel():
    def __init__(self,marca,potencia,Isc,precio,peso,altura,ancho):
        self.marca = marca
        self.potencia = potencia
        self.Isc = Isc
        self.precio = precio
        self.peso = peso
        self.altura = altura
        self.ancho = ancho
        

class cargas():
    def __init__(self,PotenciaReq,EnergiaReq):
        self.PotenciaReq = PotenciaReq 
        self.EnergiaReq = EnergiaReq


class ambiente():
    def __init__(self,HSP,latitud,longitud,altura):
        self.HSP = HSP  
        self.latitud = latitud
        self.longitud = longitud
        self.altura = altura      


panel1 = panel(10,20,12,150000,45,100,57)
print(panel1.precio) #precio del panel 1