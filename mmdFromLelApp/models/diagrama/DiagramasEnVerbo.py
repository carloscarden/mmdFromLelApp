from typing import List
from mmdFromLelApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones


from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo


class DiagramasEnVerbo:

    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama=  unDiagrama
        self.posicionVerbo = (ConstantesPosiciones.XVERBO.value , ConstantesPosiciones.YVERBO.value)
        

    def nuevoHecho(self, verbo: Lel):
        return self.diagrama.nuevoHechoDelDiagrama(verbo.simbolo, self.posicionVerbo)

    def actualizarPosicionVerbo(self):
        self.posicionVerbo = (self.posicionVerbo[0]+ConstantesPosiciones.ACTUALIZACION_X.value, 
                              self.posicionVerbo[1]+ConstantesPosiciones.ACTUALIZACION_Y.value)

                        
    def esquinasVerbo(self):
        # Calculemos la mitad del largo y del alto:
        # Posición del centro:
        ''' 
        
        El centro del rectángulo es el punto de referencia desde el cual calculamos las esquinas.
        Uso de la mitad de las dimensiones:

            -- Usamos la mitad del largo  y la mitad del alto  
            porque el centro divide el rectángulo en cuatro partes iguales.

            -- Desde el centro hasta cualquier borde lateral, la distancia es la mitad del largo.

            -- Desde el centro hasta cualquier borde superior o inferior, la distancia es la mitad del alto.

        '''


        mitadDelLargo = self.posicionVerbo[0] / 2
        mitadDelAlto= self.posicionVerbo[1] / 2

        print("mitad de largo", mitadDelLargo)
        print("mitad de alto", mitadDelAlto)

        # Cálculo de las coordenadas:
        ''' 

            Para el eje x:

               -- Restamos la mitad del largo al centro para obtener el lado izquierdo.
               -- Sumamos la mitad del largo al centro para obtener el lado derecho.
        '''
        print("posicion de verbo[0]", self.posicionVerbo[0])
        print("posicion de verbo[1]", self.posicionVerbo[1])

        xsi = self.posicionVerbo[0] - mitadDelLargo  + ConstantesPosiciones.APERTURA_NODO_VERBO_EJE_X.value

        xii = self.posicionVerbo[0] + mitadDelLargo  - ConstantesPosiciones.APERTURA_NODO_VERBO_EJE_X.value


        ''' 
        
            Para el eje y:

               -- Restamos la mitad del alto al centro para obtener el lado superior.
               -- Sumamos la mitad del alto al centro para obtener el lado inferior.
        '''
        ysi = self.posicionVerbo[1] - mitadDelAlto - ConstantesPosiciones.APERTURA_NODO_VERBO_EJE_Y.value

        yii = self.posicionVerbo[1] + mitadDelAlto  + ConstantesPosiciones.APERTURA_NODO_VERBO_EJE_Y.value


        esquinaSuperiorIzquierda = (xsi,ysi)
        esquinaSuperiorDerecha = (xii, ysi)
        esquinaInferiorIzquierda= (xsi, yii)
        esquinaInferiorDerecha = (xii, yii)
        return [esquinaSuperiorIzquierda, esquinaSuperiorDerecha, esquinaInferiorIzquierda, esquinaInferiorDerecha]


    def generarObjetosDelDiagramaPorVerbo(self, procesadoEnVerbo: ProcesadoEnVerbo, verbo: Lel, hecho: ObjetoDiagrama):
        # all the elements in lelsDeMedida should be defined as 
        # measures of the fact corresponding to v
        self.nuevasMedidasDeVerbo(procesadoEnVerbo.lelsDeMedida, verbo, hecho)
        
        
        # all the elements on lelsCategoricosDeVerbo  should be defined as 
        # dimensions of the fact corresponding to v
        self.nuevasDimensionesDeVerbo(procesadoEnVerbo.lelsCategoricosDeVerbo, verbo)


    def nuevasMedidasDeVerbo(self, lelsDeMedida: List[Lel], verboLel: Lel, hecho: ObjetoDiagrama):
        for lelMedida in lelsDeMedida:
            lelMedida.terminadoDeProcesarMedida()
            hecho.nuevaMedidaDeVerbo(lelMedida.simbolo)


    def nuevasDimensionesDeVerbo(self, lelsDeDimensiones: List[Lel], verboLel: Lel):
        for lelDimension in lelsDeDimensiones:
            posicionNueva = verboLel.getPosicionParaNodoDeVerbo()
            simboloDimension = lelDimension.simbolo
            simboloVerbo = verboLel.simbolo
            self.diagrama.nuevoObjetoDimensionDelDiagrama(simboloDimension, simboloVerbo, posicionNueva)
            self.diagrama.nuevoLinkDimensionDelDiagrama(simboloDimension, simboloVerbo)
            lelDimension.actualizarPosicionDiagrama(posicionNueva)
            lelDimension.terminadoDeDibujarNodo()


            