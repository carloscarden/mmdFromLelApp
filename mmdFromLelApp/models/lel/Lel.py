from mmdFromLelApp.models.diagrama.TipoObjetoDiagrama import TipoObjetoDiagrama
from mmdFromLelApp.models.lel.DatosParaProcesoDiagrama import DatosParaProcesoDiagrama
from spacy.tokens import Doc



class Lel:
    '''El LEL es un glosario
en el cual se definen símbolos (términos o frases), y cada símbolo se define a través
de dos atributos: la noción y los impactos'''
    
    i = 12345

    def __init__(self, categoria: str, simbolo: str, nocion: str):
        self.categoria = categoria

        self.simbolo = simbolo
        '''
        símbolos (términos o frases)
        '''

        self.nocion = nocion
        ''' 
        La noción describe la denotación, es decir, describe las características intrínsecas 
        y sustanciales del símbolo
        '''

        self.datosParaProceso = DatosParaProcesoDiagrama()
        '''
        Datos necesarios para la construccion del diagrama
        '''


    def devolverDocNotion(self, nlp) -> Doc:
        return self.datosParaProceso.miDocNotion(nlp, self.nocion)

    
    def estaProcesado(self):
        return self.datosParaProceso.procesadoLel
    
    def terminadoDeProcesar(self):
        self.datosParaProceso.procesadoLel = True

    def actualizarPosicionDiagrama(self, posicion):
        self.datosParaProceso.nuevaPosicionDiagrama(posicion)

    def getPosicionParaNodoDeVerbo(self):
        return self.datosParaProceso.calcularPosicionProximoNodoParaVerbo()

    def getPosicionParaNodoDeSujeto(self):
        return self.datosParaProceso.calcularPosicionProximoNodo()
    

    def terminadoDeProcesarVerbo(self):
        self.datosParaProceso.nuevoVerbo()

    def terminadoDeProcesarPropiedad(self):
        self.datosParaProceso.nuevaPropiedad()


    def terminadoDeProcesarMedida(self):
        self.datosParaProceso.nuevaMedidaEnVerbo()

    def __str__(self):
        return f"Lel(atributo1={self.categoria}, atributo2={self.simbolo}) "
    

    def __repr__(self) -> str:
        return f"Lel(atributo1={self.categoria}, simbolo={self.simbolo}) "