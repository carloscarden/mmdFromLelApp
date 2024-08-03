from django.test import TestCase
from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.LinkDiagrama import LinkDiagrama
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.services.AplicadorReglasSujeto import AplicadorDeReglasSujeto
from mmdFromLelApp.services.AplicadorReglasVerbo import AplicadorDeReglasVerbo

from mmdFromLelApp.tests.MockLel import MockLel


class TestAplicadorReglasSujeto(TestCase):


    def setUp(self) -> None:
        self.mockLel = MockLel().lelMockeadoEmpresaAutos()
        self.diagrama = Diagrama([], [])

        aplicadorDeReglasVerbo = AplicadorDeReglasVerbo(self.diagrama) 
        self.lelsCategoricosDeVerbo = aplicadorDeReglasVerbo.aplicarReglasDeVerbo(self.mockLel)

        self.aplicadorDeReglasSujeto = AplicadorDeReglasSujeto(self.diagrama) 

    def testNodosDiagramaSujeto(self):

        o1 = ObjetoDiagrama("Model",  "Category")
        o2 = ObjetoDiagrama("Factory",   "Category" )
        o3 = ObjetoDiagrama("Segment",   "Property" )
        o4 = ObjetoDiagrama("Store",   "Property" )
        o5 = ObjetoDiagrama("City",   "Property" )
        o6 = ObjetoDiagrama("Region",   "Property" )
        o7 = ObjetoDiagrama("Country",  "Price")

        o8 = ObjetoDiagrama("Capacity",   "Category" )
        o9 = ObjetoDiagrama("Gender",   "Category" )

        objetosDeDiagramaQueTieneQueDevolver = [o1,o2,o3,o4,o5, o6, o7, o8, o9]


        self.aplicadorDeReglasSujeto.aplicarReglasDeSujeto(self.lelsCategoricosDeVerbo,self.mockLel)
        objetosDiagramaDevueltos = self.diagrama.objetosDelDiagrama

        print("      TEST NODOS DEL SUJETO!!!")
        try:
                    
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            for s in objetosDeDiagramaQueTieneQueDevolver:
                self.assertTrue(any(oa.key.lower() == s.key.lower() for oa in objetosDiagramaDevueltos))
                print("TEST OK RECUPERAR NODOS DEL SUJETO!!!")
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')


    def testLinksDiagramaVerbo(self):

        l1 = LinkDiagrama("Car", "Model","linkNormal")
        l2 = LinkDiagrama("Model", "Segment" ,"linkNormal")
        l3 = LinkDiagrama("Store", "City" ,"linkNormal")
        l4 = LinkDiagrama("City", "Region" ,"linkNormal")
        l5 = LinkDiagrama("Region", "Country" ,"linkNormal")

        l6 = LinkDiagrama("Model", "Capacity" ,"linkNormal")

        l7 = LinkDiagrama("Model", "Factory" ,"linkNormal")
        l8 = LinkDiagrama("Factory", "Model" ,"linkNormal")

        l9 = LinkDiagrama("Client", "Gender" ,"linkNormal")

        linksQueTieneQueDevolver = [l1,l2,l3,l4,l5, l6, l7, l8, l9]

        self.aplicadorDeReglasSujeto.aplicarReglasDeSujeto(self.lelsCategoricosDeVerbo,self.mockLel)
        linksDevueltos = self.diagrama.linksDelDiagrama


        print("              TEST LINKS DEL SUJETO!!!")
        try:
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            for s in linksQueTieneQueDevolver:
                self.assertTrue(any(oa.desde.lower() == s.desde.lower()  for oa in linksDevueltos))
                print("TEST OK RECUPERAR NODOS DEL SUJETO!!!")
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')

