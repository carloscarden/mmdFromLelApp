
from typing import List

from mmdFromLelApp.models.lel.Lel import Lel


class ProcesadoEnVerbo:
    """Aca se guarda todo lo que se puede procesar en un verbo"""
    i = 12345


    def __init__(self, lelsDeMedida: List[Lel], lelsCategoricosDeVerbo: List[Lel]):
        ''' 
          lelsDeMedida be the set of objects and subjects in notion of verb that denote 
                numerical attributes
        '''

        self.lelsDeMedida=lelsDeMedida 


        ''' 
          lelsCategoricosDeVerbo be the set of objects and subjects in notion of verb that denote
                categorical attributes
        '''
        self.lelsCategoricosDeVerbo=  lelsCategoricosDeVerbo

    def nuevoLelDeMedida(self, unLelDeMedida):
        self.lelsDeMedida.append(unLelDeMedida)

    def nuevoLelCategoricoDeVerbo(self, unLelCategoricoDeVerbo: Lel, unaPosicionDiagrama):
        unLelCategoricoDeVerbo.actualizarPosicionDiagrama(unaPosicionDiagrama) 
        self.lelsCategoricosDeVerbo.append(unLelCategoricoDeVerbo)

    def devolverLelsDeMedida(self):
        if(self.lelsDeMedida):
            return self.lelsDeMedida[0].simbolo
        return ''