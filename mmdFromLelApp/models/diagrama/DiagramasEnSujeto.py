from typing import List

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.LinkDiagrama import LinkDiagrama
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto


class DiagramasEnSujeto:
    """Clase para construir los diagramas que apareceran en los sujetos
    """
    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama = unDiagrama

    
    def generarObjetosDelDiagramaPorSujeto(self, procesadoEnSujeto: ProcesadoEnSujeto, sujeto: Lel):
        # all the elements in lelsDeMedida should be defined as 
        # measures of the fact corresponding to v
        self.nuevosNivelesProcesados(procesadoEnSujeto.lelsDeNivel, sujeto)
        self.nuevosArcosMultiples(procesadoEnSujeto.lelsArcosMultiples, sujeto)
        self.nuevosArcosOpcionales(procesadoEnSujeto.lelsArcosOpcionales, sujeto)
        self.nuevosNivelesNoProcesados(procesadoEnSujeto.lelsDeNivelNoProcesados, sujeto)
        self.nuevasPropiedades(procesadoEnSujeto.lelsDePropiedad, sujeto)


    def nuevosNivelesProcesados(self,  lelsDeNivel: List[Lel], sujeto: Lel):
        for nivel in lelsDeNivel:
            self.diagrama.nuevoLinkHecho(sujeto.simbolo, nivel.simbolo)


    def nuevosArcosMultiples(self, lelsArcosMultiples: List[Lel], sujeto: Lel):
        for lelMultiple in lelsArcosMultiples:
            self.diagrama.nuevoLinkMultiple(sujeto.simbolo, lelMultiple.simbolo)
            self.nuevoNodoMultiple(sujeto, lelMultiple)

    def nuevosArcosOpcionales(self, lelsArcosOpcionales: List[Lel],sujeto: Lel):
        for lelOpcional in lelsArcosOpcionales:
            self.diagrama.nuevoLinkOpcional(sujeto.simbolo, lelOpcional.simbolo)
            self.nuevoNodoOpcional(sujeto, lelOpcional)

    def nuevosNivelesNoProcesados(self, lelsDeNivelNoProcesados: List[Lel],sujeto: Lel):
        for lelNoProcesados in lelsDeNivelNoProcesados:
            self.nuevoNodoNoProcesado(sujeto, lelNoProcesados)

    def nuevasPropiedades(self,  lelsDePropiedad: List[Lel], sujeto: Lel):
        for lelPropiedad in lelsDePropiedad:
            self.diagrama.nuevoLinkHecho(sujeto.simbolo, lelPropiedad.simbolo)
            self.nuevaPropiedad(sujeto, lelPropiedad)
            

    def nuevoNodoMultiple(self, sujeto: Lel, lelMultiple: Lel):
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelMultiple.actualizarPosicionDiagrama(posicionNueva)
            
        self.diagrama.nuevoObjetoNivelDelDiagrama(lelMultiple.simbolo, sujeto.simbolo, posicionNueva)


    def nuevoNodoOpcional(self, sujeto: Lel, lelOpcional: Lel):       
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelOpcional.actualizarPosicionDiagrama(posicionNueva)
            
        self.diagrama.nuevoObjetoOpcionalDelDiagrama(lelOpcional.simbolo, sujeto.simbolo, posicionNueva)
        lelOpcional.terminadoDeDibujarNodo()


    def nuevoNodoNoProcesado(self, sujeto: Lel, lelNoProcesado: Lel):
        if(lelNoProcesado.estaDibujado()):
            return
        
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelNoProcesado.actualizarPosicionDiagrama(posicionNueva)
        
        self.diagrama.nuevoObjetoNivelDelDiagrama(lelNoProcesado.simbolo, sujeto.simbolo, posicionNueva)
        lelNoProcesado.terminadoDeDibujarNodo()

        
    def nuevaPropiedad(self, sujeto: Lel, lelPropiedad: Lel):
        posicionNueva = sujeto.getPosicionParaNodoDeSujeto()
        lelPropiedad.actualizarPosicionDiagrama(posicionNueva)
        self.diagrama.nuevoObjetoPropiedadDelDiagrama(lelPropiedad.simbolo, sujeto.simbolo, posicionNueva)
        lelPropiedad.terminadoDeDibujarNodo()
            
