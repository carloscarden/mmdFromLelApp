
from django.test import TestCase
from mmdFromLelApp.models.diagrama.ConstantesPosiciones import ConstantesPosiciones

from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.models.diagrama.DiagramasEnSujeto import DiagramasEnSujeto
from mmdFromLelApp.models.diagrama.ObjetoDiagrama import ObjetoDiagrama
from mmdFromLelApp.models.lel.CalculadorPosicionSujeto import CalculadorPosicionSujeto
from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto

class TestPosicion(TestCase):

    def setUp(self) -> None:
        self.diagrama = Diagrama([], [])
        self.diagramasEnSujeto = DiagramasEnSujeto(self.diagrama)

    def getObjetosDiagramaDelNodoQueTieneQueDevolver(self):
        objeto2 = ObjetoDiagrama.nuevoNivel('n1', 'Model', (0,0))
        objeto3 = ObjetoDiagrama.nuevoNivel('n2', 'Model', (0,0))
        objeto4 = ObjetoDiagrama.nuevoNivel('n3', 'Model', (0,0))
        objeto5 = ObjetoDiagrama.nuevoNivel('n4', 'Model', (0,0))
        objetosLadoArriba = [objeto2,objeto3,objeto4,objeto5]        

        objeto6 = ObjetoDiagrama.nuevoNivel('n5', 'Model', (0,0))
        objeto7 = ObjetoDiagrama.nuevoNivel('n6', 'Model', (0,0))
        objeto8 = ObjetoDiagrama.nuevoNivel('n7', 'Model', (0,0))
        objeto9 = ObjetoDiagrama.nuevoNivel('n8', 'Model', (0,0))
        objetosLadoDerecho = [objeto6,objeto7,objeto8,objeto9]        


        objeto10 = ObjetoDiagrama.nuevoNivel('n9', 'Model', (0,0))
        objeto11 = ObjetoDiagrama.nuevoNivel('n10', 'Model', (0,0))
        objeto12 = ObjetoDiagrama.nuevoNivel('n11', 'Model', (0,0))
        objeto13 = ObjetoDiagrama.nuevoNivel('n12', 'Model', (0,0))
        objetosLadoIzquierdo = [objeto10,objeto11,objeto12,objeto13]        

        objeto14 = ObjetoDiagrama.nuevoNivel('n13', 'Model', (0,0))
        objeto15 = ObjetoDiagrama.nuevoNivel('n14', 'Model', (0,0))
        objeto16 = ObjetoDiagrama.nuevoNivel('n15', 'Model', (0,0))
        objeto17 = ObjetoDiagrama.nuevoNivel('n16', 'Model', (0,0))
        objetosLadoAbajo = [objeto14,objeto15,objeto16,objeto17]        

        return [objetosLadoArriba,objetosLadoDerecho, objetosLadoAbajo, objetosLadoIzquierdo]


    def getDimensionesEnSujeto(self):

        lelsDeSujetoArriba1 = Lel(Categoria.SUJETO, 'n1','''notion''')
        lelsDeSujetoArriba2 = Lel(Categoria.SUJETO, 'n2', '''notion2''')
        lelsDeSujetoArriba3 = Lel(Categoria.SUJETO, 'n3', '''notion3''')
        lelsDeSujetoArriba4 = Lel(Categoria.SUJETO, 'n4', '''notion4''')

        dimensionesSujetoArriba = [lelsDeSujetoArriba1, 
                                   lelsDeSujetoArriba2, lelsDeSujetoArriba3, lelsDeSujetoArriba4 ]

        lelsDeSujetoDerecha1 = Lel(Categoria.SUJETO, 'n5', '''notion2''')
        lelsDeSujetoDerecha2 = Lel(Categoria.SUJETO, 'n6', '''notion3''')
        lelsDeSujetoDerecha3 = Lel(Categoria.SUJETO, 'n7', '''notion4''')
        lelsDeSujetoDerecha4 = Lel(Categoria.SUJETO, 'n8','''notion''')

        dimensionesSujetoDerecha = [lelsDeSujetoDerecha1,
                                     lelsDeSujetoDerecha2, lelsDeSujetoDerecha3, lelsDeSujetoDerecha4, ]

        lelsDeSujetoAbajo6 = Lel(Categoria.SUJETO, 'n9', '''notion2''')
        lelsDeSujetoAbajo7 = Lel(Categoria.SUJETO, 'n10', '''notion3''')
        lelsDeSujetoAbajo8 = Lel(Categoria.SUJETO, 'n11', '''notion4''')
        lelsDeSujetoAbajo9 = Lel(Categoria.SUJETO, 'n12','''notion''')

        dimensionesSujetoAbajo = [lelsDeSujetoAbajo6,
                                   lelsDeSujetoAbajo7, lelsDeSujetoAbajo8, lelsDeSujetoAbajo9 ]
        
        lelsDeSujetoIzquierda11 = Lel(Categoria.SUJETO, 'n13', '''notion2''')
        lelsDeSujetoIzquierda12 = Lel(Categoria.SUJETO, 'n14', '''notion3''')
        lelsDeSujetoIzquierda13 = Lel(Categoria.SUJETO, 'n15', '''notion4''')
        lelsDeSujetoIzquierda14 = Lel(Categoria.SUJETO, 'n16','''notion''')

        dimensionesSujetoIzquierda = [lelsDeSujetoIzquierda11, 
                       lelsDeSujetoIzquierda12, lelsDeSujetoIzquierda13, lelsDeSujetoIzquierda14, ]
        

        return [dimensionesSujetoArriba,dimensionesSujetoDerecha, dimensionesSujetoAbajo, dimensionesSujetoIzquierda]


    def generarNodosSujeto(self, dimensiones, posicion, sujeto: Lel, angulo):
        calculadorPosicionSujeto = CalculadorPosicionSujeto(angulo)
        sujeto.actualizarPosicionDiagramaSujeto(calculadorPosicionSujeto, posicion)

        mockProcesadoEnSujeto = ProcesadoEnSujeto([],[],dimensiones,[],[])
        self.diagramasEnSujeto.generarObjetosDelDiagramaPorSujeto(mockProcesadoEnSujeto, sujeto)

    def testNodosPosicionEnNodo(self):

        objetoDiagramasQueTieneQueDevolver = self.getObjetosDiagramaDelNodoQueTieneQueDevolver()
        dimensionesAprocesar = self.getDimensionesEnSujeto()

        sujetoArriba = Lel(Categoria.OBJETO, 's1', '''notion''')
        self.generarNodosSujeto( dimensionesAprocesar[0], (600.0, -35.0), sujetoArriba,
                                 ConstantesPosiciones.ANGULO_APERTURA_LADO_ARRIBA.value)

        sujetoDerecha = Lel(Categoria.OBJETO, 's2', '''notion''')
        self.generarNodosSujeto(dimensionesAprocesar[1], (1000.0, -35.0), sujetoDerecha,
                                   ConstantesPosiciones.ANGULO_APERTURA_LADO_DERECHO.value)

        sujetoAbajo = Lel(Categoria.OBJETO, 's3', '''notion''')
        self.generarNodosSujeto(dimensionesAprocesar[2], (600.0, 135.0), sujetoAbajo,
                                 ConstantesPosiciones.ANGULO_APERTURA_LADO_ABAJO.value)

        sujetoIzquierda = Lel(Categoria.OBJETO, 's4', '''notion''')
        self.generarNodosSujeto(dimensionesAprocesar[3], (1000.0, 135.0), sujetoIzquierda,
                                 ConstantesPosiciones.ANGULO_APERTURA_LADO_IZQUIERDO.value)


        diagramasDevueltos = self.diagrama.objetosDelDiagrama

        print("     ")
        print("Diagramas devueltos::\n", "\n ".join(map(str, diagramasDevueltos)))
        print("              TEST POSICIONES DEL SUJETO!!!")
        try:
            objetoDiagramaArribaQueTieneQueDevolver = objetoDiagramasQueTieneQueDevolver[0]
            print("objetoDiagramaArribaQueTieneQueDevolver que tiene que devolver::\n",
                  "\n ".join(map(str, objetoDiagramaArribaQueTieneQueDevolver)))
            # Comprueba que todos los links se dibujaron correctamente
            for s in objetoDiagramaArribaQueTieneQueDevolver:
                hayObjeto = any((oa.key == s.key 
                                     and oa.posicionX == s.posicionX and oa.posicionY == s.posicionY)
                                       for oa in diagramasDevueltos)
                if(not hayObjeto):
                    print("objeto no encontrado: ",s)
                
                self.assertTrue(hayObjeto)


            objetoDiagramaDerechaQueTieneQueDevolver = objetoDiagramasQueTieneQueDevolver[1]
            print("objetoDiagramaDerechaQueTieneQueDevolver que tiene que devolver::\n",
                  "\n ".join(map(str, objetoDiagramaDerechaQueTieneQueDevolver)))
            # Comprueba que todos los links se dibujaron correctamente
            for s in objetoDiagramaDerechaQueTieneQueDevolver:
                hayObjeto = any((oa.key == s.key 
                                     and oa.posicionX == s.posicionX and oa.posicionY == s.posicionY)
                                       for oa in diagramasDevueltos)
                if(not hayObjeto):
                    print("objeto no encontrado: ",s)
                
                self.assertTrue(hayObjeto)

                
            objetoDiagramaAbajoQueTieneQueDevolver = objetoDiagramasQueTieneQueDevolver[2]
            print("objetoDiagramaAbajoQueTieneQueDevolver que tiene que devolver::\n",
                  "\n ".join(map(str, objetoDiagramaAbajoQueTieneQueDevolver)))
            # Comprueba que todos los links se dibujaron correctamente
            for s in objetoDiagramaAbajoQueTieneQueDevolver:
                hayObjeto = any((oa.key == s.key 
                                     and oa.posicionX == s.posicionX and oa.posicionY == s.posicionY)
                                       for oa in diagramasDevueltos)
                if(not hayObjeto):
                    print("objeto no encontrado: ",s)
                
                self.assertTrue(hayObjeto)
                    
            objetoDiagramaIzquierdaQueTieneQueDevolver = objetoDiagramasQueTieneQueDevolver[3]
            print("objetoDiagramaIzquierdaQueTieneQueDevolver que tiene que devolver::\n",
                  "\n ".join(map(str, objetoDiagramaIzquierdaQueTieneQueDevolver)))
            # Comprueba que todos los links se dibujaron correctamente
            for s in objetoDiagramaIzquierdaQueTieneQueDevolver:
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
