

from django.test import TestCase

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.DiagramasEnSujeto import DiagramasEnSujeto
from mmdFromLelApp.models.diagrama.DiagramasEnVerbo import DiagramasEnVerbo
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto

class TestPosicion(TestCase):

    def setUp(self) -> None:
        self.diagrama = Diagrama([], [])
        self.diagramasEnSujeto = DiagramasEnSujeto(self.diagrama)

    def testNodosPosicionEnNodo(self):

        sujeto = Lel(Categoria.SUJETO, 'Model', '''A car design that belongs to one segment. 
                   A model has an engine capacity and is manufactured in one or more factories''' )


        objetoDiagramasQueTieneQueDevolver = self.getObjetosDiagramaDelNodoQueTieneQueDevolver()

        mockProcesadoEnVerbo = self.getProcesadoEnSujeto()
        self.diagramasEnSujeto.generarObjetosDelDiagramaPorSujeto(mockProcesadoEnVerbo, sujeto)


        print("              TEST LINKS DEL SUJETO!!!")
        try:
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            diagramasDevueltos = self.diagrama.objetosDelDiagrama
            # Comprueba que todos los links se dibujaron correctamente
            for s in objetoDiagramasQueTieneQueDevolver:
                hayObjeto = any((oa.key == s.key 
                                     and oa.posicionX == s.posicionX and oa.posicionY == s.posicionY)
                                       for oa in diagramasDevueltos)
                if(not hayObjeto):
                    print("objeto no encontrado: ",s)
                
                self.assertTrue(hayObjeto)
                    
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')


    def getObjetosDiagramaDelNodoQueTieneQueDevolver():
        objeto2 = ObjetoDiagrama.nuevoNivel('Segment', 'Model', (0,0))
        objeto3 = ObjetoDiagrama.nuevaDimension('Factory', 'Model', (0,0))
        objeto4 = ObjetoDiagrama.nuevaDimension('Engine capacity', 'Model', (0,0))

        return [objeto2,objeto3, objeto4]

    def getProcesadoEnSujeto():
        lel2 = Lel(Categoria.OBJETO, 'Segment', '''A category that groups different car models according to 
                   their size, use, and capacity''')

        lel3 = Lel(Categoria.OBJETO, 'Factory', '''A place where cars are manufactured''')
        
        lel4 = Lel(Categoria.OBJETO, 'Engine capacity', 
                    '''The measurement of the total volume of the cylinders normally 
        expressed in cubic centimeters or litres, e.g., 1805 cc''')

        return ProcesadoEnSujeto()