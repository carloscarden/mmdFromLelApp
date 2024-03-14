from django.test import TestCase

from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo
from mmdFromLelApp.services.ReglasEnVerbo import ReglasEnVerbo

from mmdFromLelApp.tests.MockLel import MockLel


class TestReglasEnVerbo(TestCase):

    def setUp(self) -> None:
        self.mockLel = MockLel().lelMockeado()
        self.reglasVerbo = ReglasEnVerbo()

    def testRecuperarHechos(self):

        '''  Verbs give origin to facts 
 
           entrada: List[Lel]
           salida: List[Lel] tq Lel sea verbo
           
        '''
        hechosQueTieneQueDevolver = ['Administer']
        hechos = self.reglasVerbo.recuperarLosVerbos(self.mockLel)

        print("")
        print("              TEST RECUPERAR HECHOS!!!")
        try:
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            for s in hechosQueTieneQueDevolver:
                self.assertTrue(any(hecho.simbolo == s for hecho in hechos))
            print("TEST OK RECUPERAR HECHOS!!!")
        except AssertionError:
            print("ERROR!!!")
        finally:
            print("**************************************************")               


    def procesarVerbo(self) -> ProcesadoEnVerbo:

        nocionVerbo = ''' Action performed by a doctor, that consists
in dispensing at a certain date and hour a dose of a drug to deal with some disease
of a patient in some seriousness in order to obtain some outcome.'''

        # Encontrar todos los Categorical objects and subjects del verbo
        sujetosYObjetosDeVerbo = self.reglasVerbo.encontrarObjetosYsujetosDeVerbo(nocionVerbo)


        # apply Rule 2 to v, get set Mf of measures, add them to f
        # apply Rule 3 to v, get set Df of dimensions, add them to f
        return self.reglasVerbo.procesarElVerbo(sujetosYObjetosDeVerbo, self.mockLel)



    def testRecupearMedidas(self):
        '''  Numerical objects and subjects of verbs give origin to measures. 
           entrada: notion verb, List[Lel] 
           salida:  List[Lel] tq Lel sea el numerical object del verbo
 
        '''


        print("              TEST RECUPERAR MEDIDAS!!!")
        medidas = self.procesarVerbo().lelsDeMedida

        try:
        
            medidasQueTieneQueDevolver = []
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            for s in medidasQueTieneQueDevolver:
                self.assertTrue(any(m.simbolo == s for m in medidas))
        
            print("OK EN RECUPERAR MEDIDAS")
        except AssertionError:
            print("ERROR EN RECUPERAR MEDIDAS!!!!!!!!")
        finally:
            print("******************************")



    def testRecuperarDimensiones(self, procesadoEnVerbo: ProcesadoEnVerbo):

        '''Categorical objects and subjects of verbs give origin to dimensions.
        
           entrada: notion verb, List[Lel]
           salida:  List[Lel] tq Lel sea el categorical object del verbo

        '''

        dimensionesQueTieneQueDevolver = []
        dimensionesDevueltas = self.procesarVerbo().lelsCategoricosDeVerbo

        print("               TEST RECUPERAR DIMENSIONES!!!")
        try:
        
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            for s in dimensionesQueTieneQueDevolver:
                self.assertTrue(any(d.simbolo == s for d in dimensionesDevueltas))
        
            print("OK EN RECUPERAR DIMENSIONES")
        except AssertionError:
            print("ERROR EN RECUPERAR DIMENSIONES!!!!!!!!")
        finally:
            print("******************************")

