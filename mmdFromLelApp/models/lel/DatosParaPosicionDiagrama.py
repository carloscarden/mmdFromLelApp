import math
from mmdFromLelApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones

from mmdFromLelApp.models.lel.CalculadorPosicionVerbo import CalculadorPosicionVerbo
from mmdFromLelApp.models.lel.CalculadorPosicionSujeto import CalculadorPosicionSujeto


class DatosParaPosicionDiagrama:
    i = 12345


    def __init__(self,  unaPosicionDiagrama = None, calculadorPosicionVerbo: CalculadorPosicionVerbo = None, 
                 calculadorPosicionSujeto:CalculadorPosicionSujeto = None):
        self.posicionDiagrama = unaPosicionDiagrama
        self.anguloProximoNodo = ConstantesPosiciones.ANGULO_APERTURA_INICIAL.value
        self.calculadorPosicionVerbo = calculadorPosicionVerbo
        self.calculadorPosicionSujeto = calculadorPosicionSujeto

    @property
    def DISTANCIA_NODO(self):  # es la distancia que se va a posicionar del nodo padre
        return 100

    @property
    def APERTURA_NODO(self):  # es El ángulo de abertura en grados
        return 20

    def nuevaPosicionDiagrama(self, posicion):
        self.posicionDiagrama = posicion


    def nuevoCalculadorPosicionVerbo(self, unCalculadorPosicionVerbo):
        self.calculadorPosicionVerbo = unCalculadorPosicionVerbo

    def nuevoCalculadorPosicionSujeto(self, unCalculadorPosicionSujeto):
        self.calculadorPosicionSujeto = unCalculadorPosicionSujeto

    def calcularPosicionProximoNodo(self):
        if(self.calculadorPosicionSujeto):
            posicionAdevolver= self.calculadorPosicionSujeto.calcularPosicionProximoNodo(self.posicionDiagrama)
            return posicionAdevolver
        raise Exception("NO TIENE UN CALCULADOR DE SUJETO!!")


    def calcularPosicionProximoNodoParaVerbo(self):
        if(self.calculadorPosicionVerbo):
            posicionAdevolver= self.calculadorPosicionVerbo.calcularPosicionProximoNodo()
            self.calculadorPosicionVerbo.actualizarPosiciones()
            return posicionAdevolver
        raise Exception("NO TIENE UN CALCULADOR DE VERBO!!")
    
    def getCalculadorPosicionSujeto(self):
        if(self.calculadorPosicionVerbo):
            return self.calculadorPosicionVerbo.getCalculadorPosicionSujeto()
        raise Exception("NO TIENE UN CALCULADOR DE SUJETO!!")

    def getCalculadorSujeto(self):
        if(self.calculadorPosicionSujeto):
            return self.calculadorPosicionSujeto.getCalculadorSujeto()
        raise Exception("NO TIENE UN CALCULADOR DE SUJETO!!")



    


