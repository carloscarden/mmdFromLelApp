from spacy.tokens import Doc
from spacy.language import Language

from mmdFromLelApp.models.diagrama.TipoObjetoDiagrama import TipoObjetoDiagrama

"""El LEL es un glosario
en el cual se definen símbolos (términos o frases), y cada símbolo se define a través
de dos atributos: la noción y los impactos"""

class DatosParaProcesoDiagrama:

    i = 12345

    def __init__(self, procesado: bool, docNotion: Doc, unTipoObjetoDiagrama: str, unaPosicionDiagrama):
        # si el lel se proceso o no
        self.procesadoLel = procesado

        self.docNotion = docNotion

        self.tipoObjetoDiagrama =  unTipoObjetoDiagrama

        self.posicionDiagrama = unaPosicionDiagrama

        self.anguloProximoNodo = 30

    def calcularPosicionProximoNodo(self):
        '''
        Para encontrar el punto en el círculo que corresponde a un ángulo de 30°, 
        puedes usar las fórmulas del círculo unitario en coordenadas polares.
        Las coordenadas (x, y) de un punto en el círculo se pueden encontrar usando las siguientes fórmulas:
            x=r⋅cos(θ)
            y=r⋅sin(θ)
        Donde r es el radio del círculo y θ es el ángulo en radianes.
        '''  
        posicionX = self.calcularPosicionX()
        posicionY = self.calcularPosicionY()
        
        self.anguloProximoNodo  = self.anguloProximoNodo+30 
        return (posicionX, posicionY)

    def calcularPosicionX(self):
        pass

    def calcularPosicionY(self):
        pass

    
    def calcularPosicionProximoNodoParaVerbo():
        return 0

    
    def miDocNotion(self, nlp: Language, nocion)-> Doc:
        if(self.docNotion):
            return self.docNotion
        else:
            self.docNotion =nlp(nocion)
            return self.docNotion
 

    def nuevoVerbo(self):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.HECHO

    def nuevoNivel(self, posicion):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.NIVEL
        self.posicionDiagrama = posicion

    def nuevaPropiedad(self, posicion):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.PROPIEDAD
        self.posicionDiagrama = posicion

    def nuevaPosicionDiagrama(self, posicion):
        self.posicionDiagrama = posicion