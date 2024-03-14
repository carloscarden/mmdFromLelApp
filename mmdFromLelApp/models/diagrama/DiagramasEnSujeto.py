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


    def nuevosNiveles(self,  lelsDeNivel: List[Lel], sujeto: str):
        for lel in lelsDeNivel:
            nuevaMedida = ObjetoDiagrama.nuevoNivel(lel.simbolo, sujeto)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaMedida)


    def nuevasPropiedades(self,  lelsDePropiedad: List[Lel], sujeto: str):
        for lel in lelsDePropiedad:
            nuevaMedida = ObjetoDiagrama.nuevaPropiedad(lel.simbolo, sujeto)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaMedida)


    def nuevoLinkDelDiagrama(self, linkDelDiagrama):
        self.diagrama.nuevoLinkDelDiagrama(linkDelDiagrama)