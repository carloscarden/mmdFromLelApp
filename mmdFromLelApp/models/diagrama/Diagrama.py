from typing import List
from mmdFromLelApp.models.diagrama.LinkDiagrama import LinkDiagrama

from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.Lel import Lel

class Diagrama:
    """Clase que mantiene los objetos y los links del diagrama,
       Es la clase que se va a mandar al frontend para que consuma
    """
    i = 12345

    def __init__(self, objetosDelDiagrama: List[ObjetoDiagrama], linksDelDiagrama: List[LinkDiagrama]):
        self.objetosDelDiagrama= objetosDelDiagrama
        self.linksDelDiagrama= linksDelDiagrama


    def nuevoObjetoDelDiagrama(self, objetoDelDiagrama):
        self.objetosDelDiagrama.append(objetoDelDiagrama)


    def nuevoLinkDelDiagrama(self, linkDelDiagrama):
        self.linksDelDiagrama.append(linkDelDiagrama)

    def generarLinks(self,desdeExpresion, lelsCategoricos: List[Lel]):
        for lel in lelsCategoricos:
            nuevoLink = LinkDiagrama(desdeExpresion, lel.simbolo)
            self.linksDelDiagrama.append(nuevoLink)

