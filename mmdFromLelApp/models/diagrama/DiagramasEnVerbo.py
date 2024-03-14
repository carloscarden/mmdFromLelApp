from typing import List
from mmdFromLelApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones


from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.diagrama.TipoObjetoDiagrama import TipoObjetoDiagrama
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo


class DiagramasEnVerbo:

    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama=  unDiagrama
        self.posicionVerbo = (ConstantesPosiciones.XVERBO , ConstantesPosiciones.YVERBO)
        

    def nuevoHecho(self, verbo: Lel):
        nuevoVerbo = ObjetoDiagrama.nuevoHecho(verbo.simbolo, self.posicionVerbo)
        self.diagrama.nuevoObjetoDelDiagrama(nuevoVerbo)

    def actualizarPosicionVerbo(self):
        self.posicionVerbo = (self.posicionVerbo[0]+ConstantesPosiciones.ACTUALIZACION_X, 
                              self.posicionVerbo[1]+ConstantesPosiciones.ACTUALIZACION_Y)

    def generarObjetosDelDiagramaPorVerbo(self, procesadoEnVerbo: ProcesadoEnVerbo, simbolo: str):
        
        # all the elements in lelsDeMedida should be defined as 
        # measures of the fact corresponding to v
        self.nuevasMedidasDeVerbo(procesadoEnVerbo.lelsDeMedida, simbolo)
        
        
        # all the elements on lelsCategoricosDeVerbo  should be defined as 
        # dimensions of the fact corresponding to v
        self.nuevasDimensionesDeVerbo(procesadoEnVerbo.lelsCategoricosDeVerbo)


    def nuevasMedidasDeVerbo(self, lelsDeMedida: List[Lel], verboLel: str):
        for lel in lelsDeMedida:
            nuevaMedida = ObjetoDiagrama.nuevaMedida(lel.simbolo, verboLel)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaMedida)


    def nuevasDimensionesDeVerbo(self, lelsDeDimensiones: List[Lel], verboLel: List[Lel]):
        for lel in lelsDeDimensiones:
            nuevaMedida = ObjetoDiagrama.nuevaDimension(lel.simbolo, verboLel)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaMedida)


            