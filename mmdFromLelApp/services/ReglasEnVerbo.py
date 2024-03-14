from typing import List
import spacy
from mmdFromLelApp.models.lel.Categoria import Categoria
from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnVerbo import ProcesadoEnVerbo

from mmdFromLelApp.services.Reglas import Reglas


nlp = spacy.load("en_core_web_sm")


class ReglasEnVerbo(Reglas):

    def recuperarLosVerbos(self, lels: List[Lel]) -> List[Lel]:
          return [objeto for objeto in lels if objeto.categoria == Categoria.VERBO]


    def encontrarObjetosYsujetosDeVerbo(self, nocion: str):
        notionVerboDoc = nlp(nocion)
        # procesar notion para que me de los objetos y sujetos
        lista_simboloes = self.procesarNotion(notionVerboDoc)
        return lista_simboloes


    def procesarElVerbo(self, sujetosYObjetosDeVerbo: List[str], lelMockeado: List[Lel], verbo: Lel)-> ProcesadoEnVerbo:
        procesadoEnVerbo = ProcesadoEnVerbo([],[])
        for simbolo in sujetosYObjetosDeVerbo :
            # Encontrar el LEL correspondiente
            lelDeVerboAprocesar = list( filter( lambda obj_lel: self.esLelBuscado(obj_lel, simbolo) , 
                                           lelMockeado))
            if lelDeVerboAprocesar:
                doc =lelDeVerboAprocesar[0].devolverDocNotion(nlp)
                medidas = [tok.text for tok in doc if self.es_medida(tok.text)]
                if(len(medidas)>0):

                        # REGLA 2

                    # Numerical objects and subjects of verbs give origin to measures.
                    # buscar entre los objetos y sujetos del notion un objeto numerico
                    procesadoEnVerbo.nuevoLelDeMedida(lelDeVerboAprocesar[0])
                    
                else:
                        # REGLA 3
                    # Categorical objects and subjects of verbs give origin to dimensions
                    # Si no cae en la categoria de medida, entonces es un categorico del verbo
                    posicion = verbo.getPosicionParaNodoDeVerbo()
                    procesadoEnVerbo.nuevoLelCategoricoDeVerbo(lelDeVerboAprocesar[0], posicion)
                
        return procesadoEnVerbo    