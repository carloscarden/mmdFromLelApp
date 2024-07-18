
from typing import List
from spacy.tokens import Token

class EncontradoEnNotionSujeto:
    """ Guarda lo que pude encontrar en el notion de un sujeto """
    i = 12345

    def __init__(self, objectsSimple: List[Token], nounChunks , pluralChunks, optionalArcs: List[str]):
        self.objectsSimple=objectsSimple 
        self.nounChunks=  nounChunks
        self.pluralChunks = pluralChunks
        self.optionalArcs = optionalArcs

    def nuevoNounChunk(self, noun_chunk):
        self.nounChunks.append(noun_chunk)    

    def nuevoObjetoSimple(self, objectSimple):
        self.objectsSimple.append(objectSimple)    

    def nuevoPlural(self, nuevoPlural):
        self.pluralChunks.append(nuevoPlural)    
    
    def nuevoOptionalArc(self, objectSimple: str):
        self.optionalArcs.append(objectSimple)  

      
    def __str__(self):
        return f'''EncontradoEnSujeto(NounChunks={self.nounChunks}, objectSimple={self.objectsSimple},
                pluralChunks={self.pluralChunks},optionalArcs={self.optionalArcs}) '''
    

    def __repr__(self) -> str:
        return f'''EncontradoEnSujeto(NounChunks={self.nounChunks}, objectSimple={self.objectsSimple},
                pluralChunks={self.pluralChunks},optionalArcs={self.optionalArcs}) '''