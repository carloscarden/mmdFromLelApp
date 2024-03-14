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
            nuevaMedida = ObjetoDiagrama.nuevoNivel(lel.simbolo, sujeto, posicionNueva)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaMedida)


    def nuevasPropiedades(self,  lelsDePropiedad: List[Lel], sujeto: Lel):
        for lel in lelsDePropiedad:
            posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
            nuevaPropiedad = ObjetoDiagrama.nuevaPropiedad(lel.simbolo, sujeto.simbolo, posicionNueva)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaPropiedad)


    def nuevoLinkDelDiagrama(self, linkDelDiagrama):
        self.diagrama.nuevoLinkDelDiagrama(linkDelDiagrama)