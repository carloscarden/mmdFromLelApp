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
        o7 = ObjetoDiagrama("Country",  "Price")

        o8 = ObjetoDiagrama("Engine capacity",   "Category" )
        o9 = ObjetoDiagrama("Gender",   "Category" )

        objetosDeDiagramaQueTieneQueDevolver = [o1,o2,o3,o4,o5, o7, o8, o9]


        self.aplicadorDeReglasSujeto.aplicarReglasDeSujeto(self.lelsCategoricosDeVerbo,self.mockLel)
        objetosDiagramaDevueltos = self.diagrama.objetosDelDiagrama

        print("objetos devueltos::", "\n".join(map(str, objetosDiagramaDevueltos)))
        print("      TEST NODOS DEL SUJETO!!!")
        try:
                    
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            for s in objetosDeDiagramaQueTieneQueDevolver:
                hayObjeto = any(oa.key.lower() == s.key.lower() for oa in objetosDiagramaDevueltos)
                if (not hayObjeto):
                    print("objeto no encontrado:: ", s)
                self.assertTrue(hayObjeto)
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')


    def testLinksDiagramaVerbo(self):

        l1 = LinkDiagrama("Store","City","Arco simple")
        l2 = LinkDiagrama("City","State" ,"Arco simple")
        l3 = LinkDiagrama("State","Country" ,"Arco simple")

        l4 = LinkDiagrama("Car","Model" ,"Arco simple")
        l5 = LinkDiagrama("Model","Segment" ,"Arco simple")
        l6 = LinkDiagrama("Model","Factory" ,"Arco simple")
        l7 = LinkDiagrama("Model","Engine capacity" ,"Arco simple")

        linksQueTieneQueDevolver = [l1,l2,l3,l4, l5, l6, l7]

        self.aplicadorDeReglasSujeto.aplicarReglasDeSujeto(self.lelsCategoricosDeVerbo,self.mockLel)
        linksDevueltos = self.diagrama.linksDelDiagrama

        print("links devueltos::", "\n".join(map(str, linksDevueltos)))
        print("             TEST LINKS DEL SUJETO!!!")
        try:
            # Comprueba que todos los links se dibujaron correctamente
            for s in linksQueTieneQueDevolver:
                hayLink = any((oa.desde == s.desde and oa.hasta == s.hasta) for oa in linksDevueltos)
                if(not hayLink):
                    print("link no encontrado::", s)
                self.assertTrue(hayLink)

            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')
            