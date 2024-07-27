from django.test import TestCase
from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto
from mmdFromLelApp.services.ReglasEnSujeto import ReglasEnSujeto

from mmdFromLelApp.tests.MockLel import MockLel


class TestReglasEnSujeto(TestCase):

    def setUp(self) -> None:
        self.mockLel = MockLel().lelMockeadoEmpresaAutos()
        self.reglasSujeto = ReglasEnSujeto()


    def procesarSujeto(self, sujeto):

        # Encontrar todos los Categorical objects and subjects del sujeto
        encontradoEnSujeto  = self.reglasSujeto.encontrarLosObjetosCategoricosDeSujetos(sujeto)
        print(encontradoEnSujeto)

        #apply Rule 4 to o, get set Cl of levels, add them to l as children levels
        #apply Rule 5 to o, get set Pl of properties, add them to l as children levels
        return self.reglasSujeto.procesarElSujeto(encontradoEnSujeto, self.mockLel)


    def testRecuperarNiveles(self):

                '''Categorical objects and subjects of objects or subjects give origin to levels
                
                entrada: Model
                salida:  [segment]
                '''

                sujeto = Lel(Categoria.SUJETO, 'Model', '''A car design that belongs to one segment. A model has an engine
        capacity and is manufactured in one or more factories''' )
                
                procesadoEnSujeto = self.procesarSujeto(sujeto)


                niveles = procesadoEnSujeto.lelsDeNivel

                print("")
                print("              TEST RECUPERAR NIVELES!!!")
                try:
                    nivelesQueTieneQueDevolver = ['segment']
                    
                    print(niveles)            
                    # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
                    for s in nivelesQueTieneQueDevolver:
                        self.assertTrue(any(oa.simbolo.lower() == s.lower() for oa in niveles))
                    print("TEST OK RECUPERAR NIVELES!!!")
                except AssertionError:
                    print("ERROR!!!")
                finally:
                    print("**************************************************")  


    def testRecuperarProperties(self):
            
            '''Numerical objects and subjects of objects or subjects give origin to properties.
            
            entrada: Model
            salida:  [capacity]
            
            '''

            sujeto = Lel(Categoria.SUJETO, 'Model', '''A car design that belongs to one segment. A model has an engine
    capacity and is manufactured in one or more factories''' )
            
            properties = self.procesarSujeto(sujeto).lelsDePropiedad

            
            print("")
            print("              TEST RECUPERAR PROPERTIES!!!")
            try:
                propertiesQueTieneQueDevolver = ['Engine capacity']
                # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
                for s in propertiesQueTieneQueDevolver:
                    self.assertTrue(any(oa.simbolo.lower() == s.lower() for oa in properties))
                print("TEST OK RECUPERAR PROPERTIES!!!")
            except AssertionError:
                print("ERROR!!!")
            finally:
                print("**************************************************") 


    def testOptionalArcs(self):

            ''' Expressions of possibility in objects and subjects determine optional arcs.
            entrada:  Client
            salida:  [Gender]
            '''

            sujeto = Lel(Categoria.SUJETO, 'Client', '''A person or organization. 
                         A client may be described by gender and age''')


            optionalArcs = self.procesarSujeto(sujeto).lelsArcosOpcionales

            
            print("")
            print("              TEST RECUPERAR OPTIONAL ARCS!!!")
            try:
                optionalArcsQueTieneQueDevolver = ['Gender']
                # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
                for s in optionalArcsQueTieneQueDevolver:
                    self.assertTrue(any(oa.simbolo.lower() == s.lower() for oa in optionalArcs))
                print("TEST OK RECUPERAR OPTIONAL ARCS!!!")
            except AssertionError:
                print("ERROR!!!")
            finally:
                print("**************************************************")

    def testRecuperarMultipleArcs(self):

            '''Plural objects and subjects give origin to multiple arcs
            
            entrada:  Model
            salida:  [factory]

            '''

            sujeto = Lel(Categoria.SUJETO, 'Model', '''A car design that belongs to one segment. A model has an engine
    capacity and is manufactured in one or more factories''' )


            multipleArcs = self.procesarSujeto(sujeto).lelsArcosMultiples
            print(self.procesarSujeto(sujeto))

            print("")
            print("              TEST RECUPERAR MULTIPLE ARCS!!!")
            try:
                multipleArcsQueTieneQueDevolver = ['Factory']
                # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
                for s in multipleArcsQueTieneQueDevolver:
                    self.assertTrue(any(oa.simbolo.lower() == s.lower() for oa in multipleArcs))
                print("TEST OK RECUPERAR OPTIONAL ARCS!!!")
            except AssertionError:
                print("ERROR!!!")
            finally:
                print("**************************************************")  