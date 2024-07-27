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
    
    def nuevoHechoDelDiagrama(self, lelVerboSimbolo, posicionNueva) -> ObjetoDiagrama:
        nuevoHecho = ObjetoDiagrama.nuevoHecho(lelVerboSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevoHecho)
        return nuevoHecho

    
    def nuevoObjetoDimensionDelDiagrama(self, lelDimensionSimbolo, verboLelSimbolo, posicionNueva):
        nuevaDimension = ObjetoDiagrama.nuevaDimension(lelDimensionSimbolo, verboLelSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevaDimension)
    
    def nuevoObjetoNivelDelDiagrama(self, lelNivelSimbolo, sujetoSimbolo, posicionNueva):
        nuevoNivel = ObjetoDiagrama.nuevoNivel(lelNivelSimbolo, sujetoSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevoNivel)

    def nuevoObjetoPropiedadDelDiagrama(self, lelSimbolo, sujetoSimbolo, posicionNueva):
        nuevaPropiedad = ObjetoDiagrama.nuevaPropiedad(lelSimbolo, sujetoSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevaPropiedad)

    def nuevoObjetoOpcionalDelDiagrama(self, lelSimbolo, sujetoSimbolo, posicionNueva):
        nuevoObjetoOpcional = ObjetoDiagrama.nuevoLelOpcional(lelSimbolo, sujetoSimbolo, posicionNueva)
        self.objetosDelDiagrama.append(nuevoObjetoOpcional)
    
    
    
    def nuevoLinkDelDiagrama(self, linkDelDiagrama):
        self.linksDelDiagrama.append(linkDelDiagrama)

    def generarLinks(self,desdeExpresion, lelsCategoricos: List[Lel]):
        for lel in lelsCategoricos:
            nuevoLink = LinkDiagrama(desdeExpresion, lel.simbolo)
            self.linksDelDiagrama.append(nuevoLink)

    def to_dict(self):
            return {
                'objetosDelDiagrama': [objeto.to_dict() for objeto in self.objetosDelDiagrama],
                'linksDelDiagrama': [link.to_dict() for link in self.linksDelDiagrama]
            }
