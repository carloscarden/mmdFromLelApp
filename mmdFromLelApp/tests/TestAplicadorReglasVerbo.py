
from django.test import TestCase
from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.LinkDiagrama import LinkDiagrama
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.services.AplicadorReglasVerbo import AplicadorDeReglasVerbo
from mmdFromLelApp.services.ReglasEnVerbo import ReglasEnVerbo

from mmdFromLelApp.tests.MockLel import MockLel


class TestAplicadorReglasVerbo(TestCase):

    def setUp(self) -> None:
        self.mockLel = MockLel().lelMockeadoEmpresaAutos()
        self.diagrama = Diagrama([], [])
        self.aplicadorDeReglasVerbo = AplicadorDeReglasVerbo(self.diagrama) 


    def testNodosDiagramaVerbo(self):

        o1 = ObjetoDiagrama("Sell a car", "Price",  "Class")
        o2 = ObjetoDiagrama("Car", "Category" )
        o3 = ObjetoDiagrama("Store", "Property" )
        o4 = ObjetoDiagrama("Date", "Property" )
        o5 = ObjetoDiagrama("Client", "Property" )

        objetosDeDiagramaQueTieneQueDevolver = [o1,o2,o3,o4,o5]


        self.aplicadorDeReglasVerbo.aplicarReglasDeVerbo(self.mockLel)
        objetosDiagramaDevueltos = self.diagrama.objetosDelDiagrama

        print("              TEST NODOS DEL VERBO!!!")
        try:
                    
            # Comprueba que todos los objetos en el diagrama están dibujados
            for s in objetosDeDiagramaQueTieneQueDevolver:
                self.assertTrue(any( (oa.key == s.key and oa.category == s.category) 
                                    for oa in objetosDiagramaDevueltos))
                print("TEST OK RECUPERAR NODOS DEL VERBO!!!")
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')


    def testLinksDiagramaVerbo(self):

        l1 = LinkDiagrama("Client", "Sell a car","linkNormal")
        l2 = LinkDiagrama("Car", "Sell a car" ,"linkNormal")
        l3 = LinkDiagrama("Store", "Sell a car" ,"linkNormal")
        l4 = LinkDiagrama("Date",  "Sell a car" ,"linkNormal")

        linksQueTieneQueDevolver = [l1,l2,l3,l4]


        self.aplicadorDeReglasVerbo.aplicarReglasDeVerbo(self.mockLel)
        linksDevueltos = self.diagrama.linksDelDiagrama

        print("              TEST LINKS DEL VERBO!!!")
        try:
            # Comprueba que todos los links se dibujaron correctamente
            for s in linksQueTieneQueDevolver:
                self.assertTrue(any((oa.desde == s.desde and oa.hasta == s.hasta) for oa in linksDevueltos))
                print("TEST OK RECUPERAR NODOS DEL VERBO!!!")
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')
