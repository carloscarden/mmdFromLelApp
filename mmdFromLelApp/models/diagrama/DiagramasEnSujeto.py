from typing import List

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.Lel import Lel


class DiagramasEnSujeto:
    """Clase para construir los diagramas que apareceran en los sujetos
    """
    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama = unDiagrama


    def nuevosNiveles(self,  lelsDeNivel: List[Lel], sujeto: Lel):
        for lel in lelsDeNivel:
            posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
            lel.actualizarPosicionDiagrama(posicionNueva)
            
            self.diagrama.nuevoObjetoNivelDelDiagrama(lel.simbolo, sujeto.simbolo, posicionNueva)


    def nuevasPropiedades(self,  lelsDePropiedad: List[Lel], sujeto: Lel):
        for lel in lelsDePropiedad:
            posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
            lel.terminadoDeProcesarPropiedad()
            lel.actualizarPosicionDiagrama(posicionNueva)
            
            self.diagrama.nuevoObjetoPropiedadDelDiagrama(lel.simbolo, sujeto.simbolo, posicionNueva)

    def nuevosLelsOpcionales(self,  lelsOpcionales: List[Lel], sujeto: Lel):
        for lel in lelsOpcionales:
            posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
            lel.actualizarPosicionDiagrama(posicionNueva)
            
            self.diagrama.nuevoObjetoOpcionalDelDiagrama(lel.simbolo, sujeto.simbolo, posicionNueva)

    def nuevoLinkDelDiagrama(self, linkDelDiagrama):
        self.diagrama.nuevoLinkDelDiagrama(linkDelDiagrama)