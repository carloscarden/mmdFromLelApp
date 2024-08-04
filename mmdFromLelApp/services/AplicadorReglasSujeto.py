from typing import List

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.DiagramasEnSujeto import DiagramasEnSujeto
from mmdFromLelApp.models.diagrama.LinkDiagrama import LinkDiagrama
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto
from mmdFromLelApp.services.ReglasEnSujeto import ReglasEnSujeto



class AplicadorDeReglasSujeto():


    def __init__(self, unDiagrama: Diagrama) -> None:
        self.diagramasEnSujeto = DiagramasEnSujeto(unDiagrama)
        self.reglas = ReglasEnSujeto()

    def aplicarReglasDeSujeto(self, lelsCategoricosDeVerbo: List[Lel], lels: List[Lel]):

        lelsAprocesar = lelsCategoricosDeVerbo

        print(lelsAprocesar)


        while 1:
            hayMasLels = []

            for sujeto in  lelsAprocesar:
                print("procesando::", sujeto.simbolo)

                # Encontrar todos los Categorical objects and subjects del sujeto
                encontradoEnSujeto  = self.reglas.encontrarLosObjetosCategoricosDeSujetos(sujeto)

                #apply Rule 4 to o, get set Cl of levels, add them to l as children levels
                #apply Rule 5 to o, get set Pl of properties, add them to l as children levels
                #apply Rule 6 to o and o′, possibly change the arc from l to l′to multiple
                #apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                procesadoEnSujeto = self.reglas.procesarElSujeto(encontradoEnSujeto, lels)
                self.diagramasEnSujeto.generarObjetosDelDiagramaPorSujeto(procesadoEnSujeto, sujeto)

                
                hayMasLels.extend(procesadoEnSujeto.lelsDeNivelNoProcesados)
                print("lels para seguir procesando::", procesadoEnSujeto)
                sujeto.terminadoDeProcesar()

            if not hayMasLels:
                break
            else:
                lelsAprocesar = hayMasLels

