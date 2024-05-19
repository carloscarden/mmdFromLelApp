from typing import List

from mmdFromLelApp.models.lel.Lel import Lel

class ProcesadoEnSujeto:
    ''' Aca se guarda todo lo que se puede procesar en un sujeto'''
    i = 12345

    def __init__(self, lelsDePropiedad: List[Lel], lelsDeNivel: List[Lel], lelsDeNivelNoProcesados: List[Lel], lelsArcosOpcionales: List[Lel]):
        self.lelsDePropiedad=lelsDePropiedad
        ''' 
        lelsDePropiedad be the set of objects and subjects in subject that denote numerical attributes
        '''

        self.lelsDeNivel=  lelsDeNivel
        ''' 
         lelsDeNivel be the set of objects and subjects in subject that denote categorical attributes
        '''

        self.lelsDeNivelNoProcesados=  lelsDeNivelNoProcesados
        ''' 
         lelsDeNivelNoProcesados son los nuevos lels de nivel a dibujar y también a procesar
        '''

        self.lelsArcosOpcionales = lelsArcosOpcionales
        ''' 
         lelsArcosOpcionales son lels de arco opcional a dibujar y también a procesar
        '''

    def nuevoLelDePropiedad(self, unLelDePropiedad: Lel):
        self.lelsDePropiedad.append(unLelDePropiedad)

    def nuevoLelDeNivel(self, unLelDeNivel: Lel):
        self.lelsDeNivel.append(unLelDeNivel)

    def nuevoLelDeNivelNoProcesado(self, unLelDeNivel: Lel):
        self.lelsDeNivelNoProcesados.append(unLelDeNivel)


    def nuevoLelOpcional(self, unLelDePropiedad: Lel):
        self.lelsDePropiedad.append(unLelDePropiedad)