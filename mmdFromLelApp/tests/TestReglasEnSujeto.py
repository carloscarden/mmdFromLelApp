from django.test import TestCase
from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto
from mmdFromLelApp.services.ReglasEnSujeto import ReglasEnSujeto

from mmdFromLelApp.tests.MockLel import MockLel


class TestReglasEnSujeto(TestCase):


    def setUp(self) -> None:
        self.mockLel = MockLel().lelMockeado()
        self.reglasSujeto = ReglasEnSujeto()


    def procesarSujeto(self, sujeto: Lel):


        # Encontrar todos los Categorical objects and subjects del sujeto
        encontradoEnSujeto  = self.reglasSujeto.encontrarLosObjetosCategoricosDeSujetos(sujeto)

        #apply Rule 4 to o, get set Cl of levels, add them to l as children levels
        #apply Rule 5 to o, get set Pl of properties, add them to l as children levels
        return self.reglasSujeto.procesarElSujeto(encontradoEnSujeto, self.mockLel)



    def testRecuperarNiveles(self):

        '''Categorical objects and subjects of objects or subjects give origin to levels
        
           entrada: notion del subject, List[Lel]
           salida:  List[Lel] tq Lel sea el categorical object del sujeto
        '''

        sujeto = Lel(Categoria.SUJETO, 'Patient', ''' Person who is ill or hurt, characterized by
gender and city.''' )
        
        niveles = self.procesarSujeto(sujeto).lelsDeNivel


        nivelesQueTieneQueDevolver = []
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in nivelesQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in niveles))


    def testRecuperarProperties(self, procesadoEnSujeto: ProcesadoEnSujeto):

        '''Numerical objects and subjects of objects or subjects give origin to properties.
          
           entrada: notion del subject, List[Lel]
           salida:  List[Lel] tq Lel sea el numerical object del sujeto
        
        '''
        sujeto = Lel(Categoria.SUJETO, 'Patient', ''' Person who is ill or hurt, characterized by
gender and city.''' )

        
        properties = self.procesarSujeto(sujeto).lelsDePropiedad

        
        propertiesQueTieneQueDevolver = []
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in propertiesQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in properties))


    def testOptionalArcs(self):

        ''' Expressions of possibility in objects and subjects determine optional arcs.

        '''
        sujeto = Lel(Categoria.SUJETO, 'Patient', ''' Person who is ill or hurt, characterized by
gender and city.''' )

        niveles = self.procesarSujeto(sujeto).lelsDeNivel

        optionalArcs = [Lel]
        for nivel in niveles:
            if (self.reglasSujeto.esArcoOpcional(sujeto.devolverDocNotion(), nivel.simbolo)):
                # apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                optionalArcs.append(nivel)


        optionalArcsQueTieneQueDevolver = []
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in optionalArcsQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in optionalArcs))


    def testRecuperarMultipleArcs(self):

        '''Plural objects and subjects give origin to multiple arcs'''

        sujeto = Lel(Categoria.SUJETO, 'Patient', ''' Person who is ill or hurt, characterized by
gender and city.''' )

        niveles = self.procesarSujeto(sujeto).lelsDeNivel
        sujetoDocNotion = sujeto.devolverDocNotion()
        multipleArcs = [Lel]
        for nivel in niveles:
            if (self.reglasSujeto.esArcoMultiple(sujetoDocNotion, nivel.simbolo)):
                # apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                multipleArcs.append(nivel)


        multipleArcsQueTieneQueDevolver = []
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in multipleArcsQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in multipleArcs))


            