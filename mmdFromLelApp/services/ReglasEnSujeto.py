import spacy


from spacy.language import Language
from spacy.tokens import Token
from spacy.tokens import Doc
from spacy.tokens import Span

from typing import List

from mmdFromLelApp.models.lel.Lel import Lel
from mmdFromLelApp.models.lelsProcesados.EncontradoEnNotionSujeto import EncontradoEnNotionSujeto
from mmdFromLelApp.models.lelsProcesados.ProcesadoEnSujeto import ProcesadoEnSujeto
from mmdFromLelApp.services.Reglas import Reglas

nlp = spacy.load("en_core_web_sm")

class ReglasEnSujeto(Reglas):


    def encontrarLosObjetosCategoricosDeSujetos(self, lelsCategoricos: Lel):
        doc = lelsCategoricos.devolverDocNotion(nlp)

        # Lista de palabras objetivo
        target_words = ["has", "belongs", "comprised", "covered", "incorporated", "involves", 
                    "according","according to", "characterized by","manufactured"]

        encontradoEnSujeto = EncontradoEnNotionSujeto([],[], [], [])

        encontradoEnSujeto.optionalArcs = self.buscarPosiblesArcosOpcional(doc)


        for token in doc:
            esCompuesta = self.fraseCompuesta(token, doc, target_words)
        
            if token.text in target_words or esCompuesta:
                # Encuentra el sujeto y el objeto de la relación
                obj = [w for w in token.rights if w.dep_ == "dobj" or w.dep_ == "pobj"]

                if(esCompuesta):
                    obj = [w for w in doc[token.i + 1].rights  if w.dep_ == "dobj" or w.dep_ == "pobj"]
                else:
                    obj = [w for w in token.rights if w.dep_ == "dobj" or w.dep_ == "pobj"]


                # Busca el objeto en la lista de sustantivos y adjetivos a la derecha
                if not obj:
                    if(esCompuesta):
                        obj = [w for w in doc[token.i + 1].rights if w.dep_ == "amod" or w.dep_ == "nsubj"]
                    else:
                        obj = [w for w in token.rights if w.dep_ == "amod" or w.dep_ == "nsubj"]
            
                # Maneja las preposiciones
                if not obj:
                    if(esCompuesta):
                        obj = [w for w in doc[token.i + 1].rights if w.dep_ == "prep"]
                    else:
                        obj = [w for w in token.rights if w.dep_ == "prep"]
                    if obj:
                        obj = [w for w in obj[0].rights if w.dep_ == "pobj"]
                if obj:
                    # Find noun chunks that contain the object
                    noun_chunk = next((nc for nc in doc.noun_chunks if nc.root == obj[0] ), None)
                    self.procesarNounChunk(encontradoEnSujeto, noun_chunk)
        return encontradoEnSujeto


    def procesarNounChunk(self, encontradoEnSujeto: EncontradoEnNotionSujeto, noun_chunk: Span ):
        # Crear lista de palabras a elimina
        stop_words = ["its", "an", "a"]

        for nc in noun_chunk:
            if(nc.tag_ in ["NNS", "NNPS"]):
                encontradoEnSujeto.nuevoPlural(nc)
                return
        sinPreposiciones = [t for t in noun_chunk if t.text.lower() not in stop_words]
        if(len(sinPreposiciones) > 1):
            # palabras dobles
            encontradoEnSujeto.nuevoNounChunk(sinPreposiciones)
        else:
            encontradoEnSujeto.nuevoObjetoSimple(sinPreposiciones[0])


    def procesarElSujeto(self, encontradoEnSujeto: EncontradoEnNotionSujeto, lelMockeado: List[Lel]) -> ProcesadoEnSujeto:

        procesadoEnSujeto = ProcesadoEnSujeto([],[])
        self.procesarLosObjectsSimples(procesadoEnSujeto, encontradoEnSujeto.objectsSimple, lelMockeado)
        self.procesarLosPalabraDoble(procesadoEnSujeto, encontradoEnSujeto.nounChunks, lelMockeado)

        return procesadoEnSujeto


    def procesarLosObjectsSimples(self, procesadoEnSujeto: ProcesadoEnSujeto, 
                                   objectsSimple, lelMockeado):
        
        for simbolo in objectsSimple:
            aBuscar = simbolo.text.lower()

            lelDeSujetoAprocesar = list( filter( lambda lel: self.esLelBuscado(lel, aBuscar) , 
                                           lelMockeado))
            self.tipoDeLelQueEsElSujeto(lelDeSujetoAprocesar, procesadoEnSujeto)                               



    def procesarLosPalabraDoble(self, procesadoEnSujeto, nounChunks, lelMockeado):
        for nc in nounChunks:
            lelDeSujetoAprocesar = list( filter( lambda lel: self.esLelBuscadoCompuesto(lel, nc) , 
                                           lelMockeado))
            self.tipoDeLelQueEsElSujeto(lelDeSujetoAprocesar, procesadoEnSujeto)                               


    def tipoDeLelQueEsElSujeto(self, lelDeSujetoAprocesar:List[Lel], procesadoEnSujeto: ProcesadoEnSujeto):
        if lelDeSujetoAprocesar :
            doc = lelDeSujetoAprocesar[0].devolverDocNotion(nlp)
            medidas = [tok.text for tok in doc if self.es_medida(tok.text)]
            if(len(medidas)>0):
                     #Rule 5. 
                # Numerical objects and subjects of objects or subjects give origin to properties.
                # buscar entre los objetos y sujetos del notion un objeto numerico
                procesadoEnSujeto.nuevoLelDePropiedad(lelDeSujetoAprocesar[0])
                lelDeSujetoAprocesar[0].terminadoDeProcesarPropiedad()
            else:
                    # REGLA 4
                # Categorical objects and subjects of objects or subjects give origin to levels
                # Si no cae en la categoria de medida, entonces es un categorico del verbo
                procesadoEnSujeto.nuevoLelDeNivel(lelDeSujetoAprocesar[0])
                if(not lelDeSujetoAprocesar[0].estaProcesado):
                    procesadoEnSujeto.nuevoLelDeNivelNoProcesado(lelDeSujetoAprocesar[0])
                    lelDeSujetoAprocesar[0].terminadoDeProcesarNivel()



    def buscarPosiblesArcosOpcional(self, doc: Doc)-> List[str]:

        '''
        If the docNotion  used in n to relate o with o′ suggests that some instances
of o may not be associated to every instance of o′, then the arc from o to o′ is an optional one.
        '''    
           #         Rule 7 deals with expressions of possibility. Although simple analysis
            #could be made using a glossary of modal auxiliaries (e.g., may, might, could,
            #would, should), a more complete analysis would require some epistemic
            #expressions
        
        ''' 
        We check for adjectives with the dependency label "amod" (adjectival modifier)
          and part-of-speech tag "JJ", "JJR", or "JJS" 
          (adjective, comparative adjective, or superlative adjective). 
        We also check if the adjective has a determiner (such as "the" or "a") to its right. 
        If these conditions are met, we append the head noun of the adjective 
        (i.e., the noun that the adjective modifies) to the optional_nouns list.

        We also keep the original check for nominal subjects, 
        which will capture the subject nouns in the sentence.

        When we run this code with the example sentence ç
        "A client can be described by gender. Or, a client can be described by age.", 
        the output will be ['client', 'gender', 'client', 'age'], 
        indicating that "client" and "gender" are the nouns that express an optional attribute, 
        and "client" and "age" are the subject nouns in the sentence.
        
        '''

        optional_nouns = []
        for token in doc:
            if token.dep_ == "amod" and token.tag_ in ["JJ", "JJR", "JJS"] and any(pos.tag_ == "DT" for pos in token.rights):
                optional_nouns.append(token.head.text)
            elif token.dep_ == "nsubj" and token.tag_ in ["NN", "NNS", "NNP", "NNPS"]:
                optional_nouns.append(token.text)
        return optional_nouns    





