from mmdFromLelApp.models.diagrama.TipoObjetoDiagrama import TipoObjetoDiagrama


class ObjetoDiagrama:
    """Del diagrama representa toda la informacion para saber qué dibujar"""
    i = 12345

    def __init__(self, simbolo: str, aQuienPertenece: str, categoria = '', posicionX = 0 ,posicionY = 0):
        self.key = simbolo
        self.prop1= aQuienPertenece
        self.category= categoria
        self.posicionX =posicionX
        self.posicionY = posicionY

    @classmethod
    def nuevoHecho(self, simbolo, posicion):
        return ObjetoDiagrama(simbolo, '',  TipoObjetoDiagrama.HECHO.value, posicion[0], posicion[1])

    def nuevaMedidaDeVerbo(self, simbolo):
        self.prop1 +=simbolo + ", "
    
    @classmethod
    def nuevaMedida(self, simbolo, aQuienPertenece):
        return ObjetoDiagrama(simbolo, aQuienPertenece, TipoObjetoDiagrama.MEDIDA.value)

    @classmethod
    def nuevaDimension(self, simbolo, aQuienPertenece,posicionNueva):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.DIMENSION.value,  posicionNueva[0], posicionNueva[1])

    @classmethod
    def nuevoNivel(self, simbolo, aQuienPertenece, posicionNueva):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.NIVEL.value, posicionNueva[0], posicionNueva[1])

    @classmethod
    def nuevaPropiedad(self, simbolo, aQuienPertenece, posicionNueva):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.PROPIEDAD.value, posicionNueva[0], posicionNueva[1])

    @classmethod
    def nuevoLelOpcional(self, simbolo, aQuienPertenece, posicionNueva):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.ARCO_OPCIONAL.value, posicionNueva[0], posicionNueva[1])

    def to_dict(self):
            return {
                'key': self.key,
                'prop1': self.prop1,
                'category': self.category,
                'posicionX': self.posicionX,
                'posicionY': self.posicionY
            }


    
    def __str__(self):
        return f"Objeto(key={self.key}, prop1={self.prop1}, category={self.category} , posicion={self.posicionX, self.posicionY})"
    

    def __repr__(self) -> str:
        return f"Objeto(key={self.key}, prop1={self.prop1}, category={self.category}, posicion={self.posicionX, self.posicionY})"