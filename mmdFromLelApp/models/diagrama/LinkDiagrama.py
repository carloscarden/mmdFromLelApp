from mmdFromLelApp.models.diagrama.TipoLinkDiagrama import TipoLinkDiagrama


class LinkDiagrama:
    """Representa las conexiones que tienen los objetos del diagrama, 
    de dónde parte y a dónde llega"""
    i = 12345

    def __init__(self, desde, hasta, tipoLink: str):
        self.desde = desde
        self.hasta= hasta
        self.tipoLink = tipoLink

        
    @classmethod
    def nuevoHecho(self, desde, hasta):
        return LinkDiagrama(desde, hasta,  TipoLinkDiagrama.ARCO_SIMPLE.value)


    @classmethod
    def nuevoLinkOpcional(self, desde, hasta):
        return LinkDiagrama(desde, hasta,  TipoLinkDiagrama.ARCO_OPCIONAL.value)


    @classmethod
    def nuevoLinkMultiple(self, desde, hasta):
        return LinkDiagrama(desde, hasta,  TipoLinkDiagrama.ARCO_MULTIPLE.value)
    

    def to_dict(self):
            return {
                'desde':self.desde,
                'hasta':self.hasta,
                'tipoLink':self.tipoLink
            }