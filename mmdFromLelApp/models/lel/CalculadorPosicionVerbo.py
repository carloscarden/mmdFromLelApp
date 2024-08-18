
from mmdFromLelApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones
from mmdFromLelApp.models.diagrama.LadosDiagramaVerbo import LadosDiagramaVerbo
from mmdFromLelApp.models.lel.CalculadorPosicionSujeto import CalculadorPosicionSujeto

class CalculadorPosicionVerbo:

    i = 12345

    def __init__(self,  unasEsquinas = None, anguloNodo =None):
        self.esquinasVerbo = unasEsquinas
        self.ladoAusar = 0
        self.posiciones = [0,0,0,0]
        self.anguloNodo = anguloNodo


    def nuevaEsquinaVerbo(self, esquinasVerbo):
        self.esquinasVerbo = esquinasVerbo


    def calcularPosicionProximoNodo(self):
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_SUPERIOR.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
            self.anguloNodo = ConstantesPosiciones.ANGULO_APERTURA_LADO_ARRIBA.value
            return (posicionX, posicionY) 
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_INFERIOR.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
            self.anguloNodo = ConstantesPosiciones.ANGULO_APERTURA_LADO_ABAJO.value
            return (posicionX, posicionY) 
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_IZQUIERDO.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
            self.anguloNodo = ConstantesPosiciones.ANGULO_APERTURA_LADO_IZQUIERDO.value
            return (posicionX, posicionY) 
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_DERECHO.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
            self.anguloNodo = ConstantesPosiciones.ANGULO_APERTURA_LADO_DERECHO.value
            return (posicionX, posicionY) 


    def actualizarPosiciones(self):
        self.actualizarCorrimientosDeLosNodos()
        self.actualizarLadoAusar()


    def actualizarCorrimientosDeLosNodos(self):
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_SUPERIOR.value or 
           self.ladoAusar == LadosDiagramaVerbo.LADO_IZQUIERDO.value ):

            self.posiciones[self.ladoAusar] = self.posiciones[self.ladoAusar] + 30
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_DERECHO.value or 
           self.ladoAusar == LadosDiagramaVerbo.LADO_INFERIOR.value ):

            self.posiciones[self.ladoAusar] = self.posiciones[self.ladoAusar] + 30

    def actualizarLadoAusar(self):
        self.ladoAusar += 1
        if(self.ladoAusar == 4):
            self.ladoAusar = 0

    def getCalculadorPosicionSujeto(self):
        return CalculadorPosicionSujeto(self.anguloNodo)
