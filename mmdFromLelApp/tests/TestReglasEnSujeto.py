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
        
        niveles = self.procesarSujeto(sujeto).lelsDeNivel


        nivelesQueTieneQueDevolver = []
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in nivelesQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in niveles))


    def testRecuperarProperties(self):

        '''Numerical objects and subjects of objects or subjects give origin to properties.
          
           entrada: Model
           salida:  [capacity]
        
        '''

        sujeto = Lel(Categoria.SUJETO, 'Model', '''A car design that belongs to one segment. A model has an engine
capacity and is manufactured in one or more factories''' )
        
        properties = self.procesarSujeto(sujeto).lelsDePropiedad

        
        propertiesQueTieneQueDevolver = []
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in propertiesQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in properties))


    def testOptionalArcs(self):

        ''' Expressions of possibility in objects and subjects determine optional arcs.

        '''

        sujeto = Lel(Categoria.SUJETO, 'Client', '''A person or organization. A client may be described by gender and
age''')


        niveles = self.procesarSujeto(sujeto).lelsDeNivel
        
        # Encontrar todos los Categorical objects and subjects del verbo
        encontradoEnSujeto  = self.reglasSujeto.encontrarLosObjetosCategoricosDeSujetos(sujeto)

        optionalArcs = [Lel]
        for nivel in niveles:
            if (  any(oa == nivel.simbolo for oa in encontradoEnSujeto.optionalArcs) ):
                # apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                optionalArcs.append(nivel)


        optionalArcsQueTieneQueDevolver = ['Gender']
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in optionalArcsQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in optionalArcs))


    def testRecuperarMultipleArcs(self):

        '''Plural objects and subjects give origin to multiple arcs
        
           entrada: Model
           salida:  [factory]

        '''

        sujeto = Lel(Categoria.SUJETO, 'Model', '''A car design that belongs to one segment. A model has an engine
capacity and is manufactured in one or more factories''' )


        niveles = self.procesarSujeto(sujeto).lelsDeNivel


        # Encontrar todos los Categorical objects and subjects del verbo
        encontradoEnSujeto  = self.reglasSujeto.encontrarLosObjetosCategoricosDeSujetos(sujeto)


        multipleArcs = [Lel]
        for nivel in niveles:
            if (  any(pc == nivel.simbolo for pc in encontradoEnSujeto.pluralChunks) ):
                # apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                multipleArcs.append(nivel)


        multipleArcsQueTieneQueDevolver = []
        # Comprueba que todos los simbolos en hechosQueTieneQueDevolver están en resultado
        for s in multipleArcsQueTieneQueDevolver:
            self.assertTrue(any(oa.simbolo == s for oa in multipleArcs))


            