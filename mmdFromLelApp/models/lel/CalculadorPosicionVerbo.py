
from mmdFromLelApp.models.diagrama.LadosDiagramaVerbo import LadosDiagramaVerbo


class CalculadorPosicionVerbo:

    i = 12345

    def __init__(self,  unasEsquinas = None):
        self.esquinasVerbo = unasEsquinas
        self.ladoAusar = 0
        self.posiciones = [0,0,0,0]


    def nuevaEsquinaVerbo(self, esquinasVerbo):
        self.esquinasVerbo = esquinasVerbo


    def calcularPosicionProximoNodo(self):
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_SUPERIOR.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
            return (posicionX, posicionY) 
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_INFERIOR.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
            return (posicionX, posicionY) 
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_IZQUIERDO.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
            return (posicionX, posicionY) 
        if(self.ladoAusar == LadosDiagramaVerbo.LADO_DERECHO.value):
            posicionX = self.esquinasVerbo[self.ladoAusar][0] + self.posiciones[self.ladoAusar]
            posicionY = self.esquinasVerbo[self.ladoAusar][1]
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