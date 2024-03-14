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

        self.posicionProximoNodo = self.calcularPosicionProximoNodo()

    def calcularPosicionProximoNodo(self):
        if(self.posicionProximoNodo):
            return (self.posicionProximoNodo[0]+20, self.posicionProximoNodo[1]+30)
        elif(self.posicionDiagrama):
            return (self.posicionDiagrama[0]+20, self.posicionDiagrama[1]+30)
        else:
            return (0,0)
        
    
    def miDocNotion(self, nlp: Language, nocion)-> Doc:
        if(self.docNotion):
            return self.docNotion
        else:
            self.docNotion =nlp(nocion)
            return self.docNotion
 

    def nuevoVerbo(self, posicion):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.HECHO
        self.posicionDiagrama = posicion

    def nuevoNivel(self, posicion):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.NIVEL
        self.posicionDiagrama = posicion

    def nuevaPropiedad(self, posicion):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.PROPIEDAD
        self.posicionDiagrama = posicion

