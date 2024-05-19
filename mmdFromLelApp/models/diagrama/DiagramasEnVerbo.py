from typing import List
from mmdFromLelApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones


from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo


class DiagramasEnVerbo:

    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama=  unDiagrama
        self.posicionVerbo = (ConstantesPosiciones.XVERBO.value , ConstantesPosiciones.YVERBO.value)
        

    def nuevoHecho(self, verbo: Lel):
        self.diagrama.nuevoHechoDelDiagrama(verbo.simbolo, self.posicionVerbo)

    def actualizarPosicionVerbo(self):
        self.posicionVerbo = (self.posicionVerbo[0]+ConstantesPosiciones.ACTUALIZACION_X.value, 
                              self.posicionVerbo[1]+ConstantesPosiciones.ACTUALIZACION_Y.value)

    def generarObjetosDelDiagramaPorVerbo(self, procesadoEnVerbo: ProcesadoEnVerbo, verbo: Lel):
        
        # all the elements in lelsDeMedida should be defined as 
        # measures of the fact corresponding to v
        self.nuevasMedidasDeVerbo(procesadoEnVerbo.lelsDeMedida, verbo)
        
        
        # all the elements on lelsCategoricosDeVerbo  should be defined as 
        # dimensions of the fact corresponding to v
        self.nuevasDimensionesDeVerbo(procesadoEnVerbo.lelsCategoricosDeVerbo, verbo)


    def nuevasMedidasDeVerbo(self, lelsDeMedida: List[Lel], verboLel: Lel):
        for lelMedida in lelsDeMedida:
            lelMedida.terminadoDeProcesarMedida()
            
            self.diagrama.nuevoObjetoMedidaDeVerboDelDiagrama(lelMedida.simbolo, verboLel.simbolo)


    def nuevasDimensionesDeVerbo(self, lelsDeDimensiones: List[Lel], verboLel: Lel):
        for lelDimension in lelsDeDimensiones:
            posicionNueva = verboLel.getPosicionParaNodoDeVerbo()
            lelDimension.actualizarPosicionDiagrama(posicionNueva)
            self.diagrama.nuevoObjetoDimensionDelDiagrama(lelDimension.simbolo, verboLel.simbolo, posicionNueva)


            