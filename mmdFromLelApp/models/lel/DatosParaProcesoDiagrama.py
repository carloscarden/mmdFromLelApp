from spacy.tokens import Doc
from spacy.language import Language

from mmdFromLelApp.models.diagrama.TipoObjetoDiagrama import TipoObjetoDiagrama


class DatosParaProcesoDiagrama:

    i = 12345

    def __init__(self, procesado: bool = False, docNotion: Doc = None, 
                 unTipoObjetoDiagrama: str = None, unaPosicionDiagrama = None):
        # si el lel se proceso o no
        self.procesadoLel = False

        self.creadoEnDiagrama = False

        self.docNotion = docNotion

        self.tipoObjetoDiagrama =  unTipoObjetoDiagrama

        self.posicionDiagrama = unaPosicionDiagrama

        self.anguloProximoNodo = 30


    def miDocNotion(self, nlp: Language, nocion)-> Doc:
        if(self.docNotion):
            return self.docNotion
        else:
            self.docNotion =nlp(nocion)
            return self.docNotion
 
    def nuevoVerbo(self):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.HECHO
    
    def nuevaPropiedad(self):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.PROPIEDAD

    def nuevoNivel(self):
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.NIVEL

    def nuevaMedidaEnVerbo(self):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.MEDIDA

    def nuevoArcoOpcional(self):
        self.procesadoLel = True
        self.tipoObjetoDiagrama = TipoObjetoDiagrama.ARCO_OPCIONAL

    def nuevaPosicionDiagrama(self, posicion):
        self.posicionDiagrama = posicion

    def terminadoDeDibujarNodo(self):
        self.creadoEnDiagrama = True

    def estaDibujado(self):
        return self.creadoEnDiagrama