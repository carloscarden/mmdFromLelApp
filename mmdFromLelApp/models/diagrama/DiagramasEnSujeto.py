from typing import List

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.LinkDiagrama import LinkDiagrama
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


    def nuevoLinkHecho(self, sujetoSimbolo, nivelSimbolo):
        link= LinkDiagrama.nuevoHecho( sujetoSimbolo, nivelSimbolo)
        self.nuevoLinkDelDiagrama(link)

    def nuevoLinkMultiple(self, sujetoSimbolo, lelMultipleSimbolo):
        link = LinkDiagrama.nuevoLinkMultiple( sujetoSimbolo, lelMultipleSimbolo)
        self.nuevoLinkDelDiagrama(link)

    def nuevoLinkOpcional(self, sujetoSimbolo, lelOpcionalSimbolo):       
        link= LinkDiagrama.nuevoLinkOpcional(sujetoSimbolo, lelOpcionalSimbolo)
        self.nuevoLinkDelDiagrama(link)



    def nuevoNodoMultiple(self, sujeto: Lel, lelMultiple: Lel):
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelMultiple.actualizarPosicionDiagrama(posicionNueva)
            
        self.diagrama.nuevoObjetoNivelDelDiagrama(lelMultiple.simbolo, sujeto.simbolo, posicionNueva)


    def nuevoNodoOpcional(self, sujeto: Lel, lelOpcional: Lel):       
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelOpcional.actualizarPosicionDiagrama(posicionNueva)
            
        self.diagrama.nuevoObjetoOpcionalDelDiagrama(lelOpcional.simbolo, sujeto.simbolo, posicionNueva)


    def nuevoNodoNoProcesado(self, sujeto: Lel, lelNoProcesado: Lel):
        if(lelNoProcesado.estaDibujado()):
            return
        
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelNoProcesado.actualizarPosicionDiagrama(posicionNueva)
        
        self.diagrama.nuevoObjetoNivelDelDiagrama(lelNoProcesado.simbolo, sujeto.simbolo, posicionNueva)
        lelNoProcesado.terminadoDeDibujarNodo()

        