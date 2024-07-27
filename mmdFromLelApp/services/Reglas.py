
import spacy


from spacy.language import Language
from spacy.tokens import Token
from spacy.tokens import Doc
from spacy.tokens import Span

from nltk.corpus import wordnet
from typing import List
from mmdFromLelApp.models.lel.Categoria import Categoria

from mmdFromLelApp.models.lel.Lel import Lel

class Reglas:

    def procesarNotion(self, doc: Doc) -> List[str]:
        # Lista para almacenar los objetos encontrados
        objetos_y_sujetos = []
        # Recorrer los tokens y verificar si son objetos 
        for token in doc:
            # Verificar si el token es un sustantivo
            if token.pos_ == "NOUN" :
                objetos_y_sujetos.append(token.text)
        return objetos_y_sujetos


    def es_medida(self, doc):
        # Lista de palabras para buscar en inglés
        palabras_buscar = ["amount", "size", "height", "measure", "measurement"]
        for token in doc:
            # Verificar si el token está en nuestra lista de palabras y es relevante
            if token.text.lower() in palabras_buscar and self.es_palabra_relevante(token):
                # Buscar sus hijos en el árbol de dependencias
                for hijo in token.children:
                    # Verificar si el hijo es un complemento del nombre o una preposición
                    if hijo.dep_ in ["nmod", "prep", "relcl", "pobj"]:
                        return self.obtener_complemento_completo(hijo)
        
        # Si no se encuentra ningún complemento válido
        return []

    def es_palabra_relevante(self, token):
        # Verifica si el token es un sustantivo 
        # considere palabras que sean la raíz de la oración o hijos directos de la raíz
        return token.pos_ == "NOUN" and (token.dep_ in ["nsubj", "nsubjpass", "ROOT"] or token.head.pos_ == "ROOT")
    
    def obtener_complemento_completo(self, token):
        complemento = []
        for hijo in token.subtree:
            if hijo != token:
                complemento.append(hijo.text)
        return ' '.join(complemento)

    def fraseCompuesta(self, token: Token, doc: Doc, target_words: List[str]) -> bool:
        if token.i < len(doc) - 1:
            target_phrase = token.text + " " + doc[token.i + 1].text
            return target_phrase in target_words
        return False


    def esLelBuscado(self, unLel: Lel, simboloAbuscar: str):
        ''' Dado un string se fija si el simbolo del lel coincide y es distinto de un verbo'''
        return  unLel.simbolo.lower()==  simboloAbuscar and unLel.categoria != Categoria.VERBO


    def esLelBuscadoCompuesto(self, unLel: Lel, simboloAbuscar):
        completo = "".join([ n.text for n in simboloAbuscar]).strip().replace(",","").replace("\n"," ")
        ultimo  = simboloAbuscar[-1].text.strip()
        return ( unLel.simbolo.lower().strip() ==  completo.lower() and unLel.categoria != Categoria.VERBO ) or \
               ( unLel.simbolo.lower().strip() ==  ultimo.lower() and unLel.categoria != Categoria.VERBO )
    


        