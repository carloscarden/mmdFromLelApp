from django.test import TestCase

from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo
from mmdFromLelApp.services.ReglasEnVerbo import ReglasEnVerbo

from mmdFromLelApp.tests.MockLel import MockLel


class TestReglasEnVerbo(TestCase):

    def setUp(self) -> None:
        self.mockLel = MockLel().lelMockeadoEmpresaAutos()
        self.reglasVerbo = ReglasEnVerbo()
        self.verbo = Lel(Categoria.VERBO,  'Sell a car', ''' Operation in which a client pays a price to obtain a car on a date in
a store.''')


    def testRecuperarHechos(self):

        '''  Testeo primera regla de los Verbos para los lels correspondientes a una empresa de autos. 
        Verbs give origin to facts 
 
           entrada: lelMockeadoEmpresaAutos
           salida:  "Sell a Car" 
           
        '''
        hechosQueTieneQueDevolver = ['Sell a car']
        hechos = self.reglasVerbo.recuperarLosVerbos(self.mockLel)

        print("")
        print("              TEST RECUPERAR HECHOS!!!")
        try:
            # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
            for s in hechosQueTieneQueDevolver:
                self.assertTrue(any(hecho.simbolo.lower() == s.lower() for hecho in hechos))
            print("TEST OK RECUPERAR HECHOS!!!")
        except AssertionError:
            print("ERROR!!!")
        finally:
            print("**************************************************")               


    def procesarVerbo(self) -> ProcesadoEnVerbo:

        sujetosYObjetosDeVerbo = self.reglasVerbo.encontrarObjetosYsujetosDeVerbo(self.verbo.nocion)

        # apply Rule 2 to v, get set Mf of measures, add them to f
        # apply Rule 3 to v, get set Df of dimensions, add them to f
        return self.reglasVerbo.procesarElVerbo(sujetosYObjetosDeVerbo, self.mockLel, self.verbo)


    def testRecupearMedidas(self):
        '''  Testeo 2da regla de los Verbos para los lels correspondientes a una empresa de autos. 
           Numerical objects and subjects of verbs give origin to measures. 

              entrada: 'Sell a Car'
              salida:  ['Price']
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



    def testRecuperarDimensiones(self):

        '''
        Testeo 3ra regla de los Verbos para los lels correspondientes a una empresa de autos. 
        Categorical objects and subjects of verbs give origin to dimensions.
        
           entrada: 'Sell a Car'
           salida:  ['Car', 'Store', 'Date', 'Client]

        '''

        dimensionesQueTieneQueDevolver = ['Car', 'Store', 'Date', 'Client']
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


