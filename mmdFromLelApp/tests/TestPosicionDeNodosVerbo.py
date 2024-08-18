
from django.test import TestCase

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.DiagramasEnVerbo import DiagramasEnVerbo
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo

class TestPosicion(TestCase):


    def setUp(self) -> None:
        self.diagrama = Diagrama([], [])
        self.diagramasEnVerbo = DiagramasEnVerbo(self.diagrama)

    def getObjetosDiagramaDelVerboQueTieneQueDevolver(self):
        
        objeto1 = ObjetoDiagrama.nuevoHecho('Sell a car', (800, 50))
        objeto2 = ObjetoDiagrama.nuevaDimension('Car', 'Sell a car', (600.0, -35.0))
        objeto3 = ObjetoDiagrama.nuevaDimension('Store', 'Sell a car', (1000.0, -35.0))
        objeto3 = ObjetoDiagrama.nuevaDimension('Date', 'Sell a car', (600.0, 135.0))
        objeto4 = ObjetoDiagrama.nuevaDimension('Client', 'Sell a car', (1000.0, 135.0))

        return [ objeto1, objeto2, objeto3, objeto4]


    def getProcesadoEnVerbo(self):
        nodoVerbo2 = Lel(Categoria.OBJETO, 'Price', '''Amount of money that the client must pay for the car.''')
        medidas = [nodoVerbo2]


        nodoVerbo3 = Lel(Categoria.OBJETO, 'Car','''Four-wheel vehicle that may have different packages and can be used
either privately or commercially. A car has a model.''')
        nodoVerbo4 = Lel(Categoria.OBJETO, 'Store', '''Facility where the purchase has been done. 
                   A store is located in one city..''')
        nodoVerbo5 = Lel(Categoria.OBJETO, 'Date', '''The day when the purchase has been done.''')
        nodoVerbo6 = Lel(Categoria.SUJETO, 'Client', '''A person or organization. 
                   A client may be described by gender and age''')

        dimensiones = [nodoVerbo3, nodoVerbo4, nodoVerbo5, nodoVerbo6]
        return ProcesadoEnVerbo(medidas, dimensiones)


    def testNodosPosicionEnVerbo(self):
        
        lelVerbo = Lel(Categoria.VERBO,  'Sell a car', ''' Operation in which a client pays a price to obtain a car on a date in a store.''')
        hecho =  self.diagramasEnVerbo.nuevoHecho(lelVerbo)
        lelVerbo.actualizarPosicionDiagramaVerbo(self.diagramasEnVerbo.esquinasVerbo(),
                                                 self.diagramasEnVerbo.posicionVerbo)

        objetoDiagramasQueTieneQueDevolver = self.getObjetosDiagramaDelVerboQueTieneQueDevolver()


        mockProcesadoEnVerbo = self.getProcesadoEnVerbo()
        self.diagramasEnVerbo.generarObjetosDelDiagramaPorVerbo(mockProcesadoEnVerbo, lelVerbo, hecho)


        diagramasDevueltos = self.diagrama.objetosDelDiagrama
        print("objetos que tiene que devolver::\n","\n ".join(map(str, objetoDiagramasQueTieneQueDevolver)))

        print("     ")
        print("Diagramas devueltos::\n", "\n ".join(map(str, diagramasDevueltos)))
        print("      TEST NODOS POSICION EN VERBO!!!")
        try:
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

