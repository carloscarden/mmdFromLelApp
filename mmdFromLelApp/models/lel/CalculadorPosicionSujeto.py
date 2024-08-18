import math


from mmdFromLelApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones
from mmdFromLelApp.models.diagrama.LadosDiagramaVerbo import LadosDiagramaVerbo

class CalculadorPosicionSujeto:

    i = 12345

    def __init__(self,    unAnguloProximoNodo):
        self.anguloOriginal =unAnguloProximoNodo 
        self.anguloProximoNodo = unAnguloProximoNodo

    @property
    def DISTANCIA_NODO(self):  # es la distancia que se va a posicionar del nodo padre
        return 100

    @property
    def APERTURA_NODO(self):  # es El ángulo de abertura en grados
        return 20


    def calcularPosicionProximoNodo(self, posicionDiagrama):
        '''
    Supongamos que el ángulo de abertura es θ (theta), medido en sentido antihorario desde el eje x positivo.
    La distancia entre los puntos es n.
    Las fórmulas para calcular x1 y y1 son:
        x1 = x + n * cos(θ)

        Como el eje y está invertido, se necesita invertir el signo de esta operación:
        y1 = y - n * sin(θ)

        Donde:
            x, y son las coordenadas del punto inicial
            n es la distancia
            θ es el ángulo de abertura en radianes

    Para usar estas fórmulas, se necesita:

        Las coordenadas iniciales (x, y)
        La distancia n
        El ángulo de abertura θ en radianes 
        (si lo tienes en grados, multiplica por π/180 para convertirlo a radianes)
        '''  

        # convert degree to radian
        radian = math.radians(self.anguloProximoNodo)
        posicionX = posicionDiagrama[0] + self.DISTANCIA_NODO*math.cos(radian)

        posicionY = posicionDiagrama[1] - self.DISTANCIA_NODO*math.sin(radian)
        
        self.anguloProximoNodo  = self.anguloProximoNodo + self.APERTURA_NODO 
        return (int(posicionX), int(posicionY))

    def getCalculadorSujeto(self):
        return CalculadorPosicionSujeto(self.anguloOriginal)  

