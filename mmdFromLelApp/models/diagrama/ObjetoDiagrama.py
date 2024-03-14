from mmdFromLelApp.models.diagrama.TipoObjetoDiagrama import TipoObjetoDiagrama


class ObjetoDiagrama:
    """Del diagrama representa toda la informacion para saber qué dibujar"""
    i = 12345

    def __init__(self, simbolo, aQuienPertenece, categoria, posicionX,posicionY):
        self.key = simbolo
        self.prop1= aQuienPertenece
        self.category= categoria
        self.posicionX =posicionX
        self.posicionY = posicionY

    @classmethod
    def nuevoHecho(self, simbolo, posicion):
        return ObjetoDiagrama(simbolo, '',  TipoObjetoDiagrama.HECHO, posicion[0], posicion[1])
    
    @classmethod
    def nuevaMedida(self, simbolo, aQuienPertenece):
        return ObjetoDiagrama(simbolo, aQuienPertenece, TipoObjetoDiagrama.MEDIDA)

    @classmethod
    def nuevaDimension(self, simbolo, aQuienPertenece):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.DIMENSION)


    @classmethod
    def nuevoNivel(self, simbolo, aQuienPertenece, posicionNueva):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.NIVEL, posicionNueva[0], posicionNueva[1])

    @classmethod
    def nuevaPropiedad(self, simbolo, aQuienPertenece, posicionNueva):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.PROPIEDAD, posicionNueva[0], posicionNueva[1])
