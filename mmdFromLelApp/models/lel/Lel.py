from mmdFromLelApp.models.diagrama.TipoObjetoDiagrama import TipoObjetoDiagrama
from mmdFromLelApp.models.lel.DatosParaProcesoDiagrama import DatosParaProcesoDiagrama
from spacy.tokens import Doc

class Lel:
    
    i = 12345

    def __init__(self, categoria: str, simbolo: str, nocion: str):
        self.categoria = categoria

        '''
        símbolos (términos o frases)
        '''
        self.simbolo = simbolo

        ''' 
        La noción describe la denotación, es decir, describe las características intrínsecas 
        y sustanciales del símbolo
        '''
        self.nocion = nocion

        '''
        Datos necesarios para la construccion del diagrama
        '''
        self.datosParaProceso = DatosParaProcesoDiagrama()


    def devolverDocNotion(self, nlp) -> Doc:
        return self.datosParaProceso.miDocNotion(nlp, self.nocion)

    def terminadoDeProcesarVerbo(self):
        self.datosParaProceso.nuevoVerbo()

    def terminadoDeProcesarNivel(self, posicion):
        self.datosParaProceso.nuevoNivel(posicion)

    def terminadoDeProcesarPropiedad(self, posicion):
        self.datosParaProceso.nuevaPropiedad(posicion)

    def estaProcesado(self):
        return self.datosParaProceso.procesadoLel

    def actualizarPosicionDiagrama(self, posicion):
        self.datosParaProceso.nuevaPosicionDiagrama(posicion)

    def getPosicionParaNodoDeVerbo(self):
        return self.datosParaProceso.calcularPosicionProximoNodoParaVerbo()

    def getPosicionParaNodoDeSujeto(self):
        return self.datosParaProceso.calcularPosicionProximoNodo()