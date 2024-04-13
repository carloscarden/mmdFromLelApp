from enum import Enum

class Categoria(Enum):

    ''' 
Los símbolos se categorizan en una de cuatro categorías básicas con el fin de especializar la descripción
de los atributos. Las cuatro categorías básicas son: sujeto, objeto, verbo y estado
'''
    VERBO = 1
    ''' 
    los verbos son las acciones que realizan los sujetos sobre los objetos.
    '''

    OBJETO = 2
    ''' 
     los objetos se corresponden con elementos pasivos
    '''

    SUJETO = 3
    ''' 
    Los sujetos se corresponden con elementos activos dentro del contexto de la aplicación,
    '''
