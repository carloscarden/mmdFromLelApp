from typing import List

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.DiagramasEnSujeto import DiagramasEnSujeto
from mmdFromLelApp.models.diagrama.LinkDiagrama import LinkDiagrama
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.services.ReglasEnSujeto import ReglasEnSujeto




class AplicadorDeReglasSujeto():


    def __init__(self, unDiagrama: Diagrama) -> None:
        self.diagramasEnSujeto = DiagramasEnSujeto(unDiagrama)
        self.reglas = ReglasEnSujeto()


    def aplicarReglasDeSujeto(self, lelsCategoricosDeVerbo: List[Lel], lels: List[Lel]):

        lelsAprocesar = lelsCategoricosDeVerbo

        while 1:
            hayMasLels = []

            for sujeto in  lelsAprocesar:

                # Encontrar todos los Categorical objects and subjects del verbo
                encontradoEnSujeto  = self.reglas.encontrarLosObjetosCategoricosDeSujetos(sujeto)

                #apply Rule 4 to o, get set Cl of levels, add them to l as children levels
                #apply Rule 5 to o, get set Pl of properties, add them to l as children levels
                procesadoEnSujeto = self.reglas.procesarElSujeto(encontradoEnSujeto, lels)

                niveles = procesadoEnSujeto.lelsDeNivel

                for nivel in niveles:
                    link = None
                    if(self.reglas.esArcoMultiple(encontradoEnSujeto.pluralChunks, nivel.simbolo)):
                        # apply Rule 6 to o and o′, possibly change the arc from l to l′to multiple
                        link = LinkDiagrama.nuevoLinkMultiple( sujeto.simbolo, nivel.simbolo)
                    elif (self.reglas.esArcoOpcional(sujeto.datosParaProceso.docNotion, nivel.simbolo)):
                        # apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                        link= LinkDiagrama.nuevoLinkOpcional( sujeto.simbolo, nivel.simbolo)
                    else:
                        link= LinkDiagrama.nuevoHecho( sujeto.simbolo, nivel.simbolo)
                    self.diagramasEnSujeto.nuevoLinkDelDiagrama(link)


                hayMasLels.extend(procesadoEnSujeto.lelsDeNivelNoProcesados)
                self.diagramasEnSujeto.nuevasPropiedades(procesadoEnSujeto.lelsDePropiedad, sujeto)
                self.diagramasEnSujeto.nuevosNiveles(procesadoEnSujeto.lelsDeNivelNoProcesados, sujeto)

            if not hayMasLels:
                break
            else:
                lelsAprocesar = hayMasLels


