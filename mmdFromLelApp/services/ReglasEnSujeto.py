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
        
            #      REGLA 7 
            # deals with expressions of possibility. Although simple analysis
            # could be made using a glossary of modal auxiliaries (e.g., may, might, could,
            # would, should), a more complete analysis would require some epistemic
            # expressions
            if token.tag_ == 'MD':
                for descendant in token.head.subtree:
                    if descendant.dep_ in ['dobj', 'attr', 'pobj', 'conj']:
                        encontradoEnSujeto.nuevoOptionalArc(descendant.text) 
        return encontradoEnSujeto


    def procesarNounChunk(self, encontradoEnSujeto: EncontradoEnNotionSujeto, noun_chunk: Span ):
        # Crear lista de palabras a elimina
        stop_words = ["its", "an", "a", "one"]

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

        procesadoEnSujeto = ProcesadoEnSujeto([],[], [], [])
        self.procesarLosArcosOpcionales(procesadoEnSujeto, encontradoEnSujeto.optionalArcs, lelMockeado)
        self.procesarLosObjectsSimples(procesadoEnSujeto, encontradoEnSujeto.objectsSimple, lelMockeado)
        self.procesarLosPalabraDoble(procesadoEnSujeto, encontradoEnSujeto.nounChunks, lelMockeado)

        return procesadoEnSujeto

    def procesarLosArcosOpcionales(self, procesadoEnSujeto: ProcesadoEnSujeto, 
                                   arcosOpcionales: List[str], lelMockeado: List[Lel]):
        
        for simbolo in arcosOpcionales:
            aBuscar = simbolo.lower()

            lelDeSujetoAprocesar = list( filter( lambda lel: self.esLelBuscado(lel, aBuscar) , 
                                           lelMockeado))

            if(lelDeSujetoAprocesar):
                procesadoEnSujeto.nuevoLelOpcional(lelDeSujetoAprocesar[0])


    def procesarLosObjectsSimples(self, procesadoEnSujeto: ProcesadoEnSujeto, 
                                   objectsSimple: List[Token], lelMockeado: List[Lel]):
        

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
            medidas = self.es_medida(doc)

            if(len(medidas)>0):
                     #REGLA 5. 
                # Numerical objects and subjects of objects or subjects give origin to properties.
                # buscar entre los objetos y sujetos del notion un objeto numerico
                procesadoEnSujeto.nuevoLelDePropiedad(lelDeSujetoAprocesar[0])
            else:
                    # REGLA 4
                # Categorical objects and subjects of objects or subjects give origin to levels
                # Si no cae en la categoria de medida, entonces es un categorico del verbo
                procesadoEnSujeto.nuevoLelDeNivel(lelDeSujetoAprocesar[0])
                if(not lelDeSujetoAprocesar[0].estaProcesado):
                    procesadoEnSujeto.nuevoLelDeNivelNoProcesado(lelDeSujetoAprocesar[0])








