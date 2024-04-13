from rest_framework.response import Response
from rest_framework.views import APIView
from mmdFromLelApp.models.diagrama.Diagrama import Diagrama
from mmdFromLelApp.services.AplicadorReglasSujeto import AplicadorDeReglasSujeto
from mmdFromLelApp.services.AplicadorReglasVerbo import AplicadorDeReglasVerbo

from mmdFromLelApp.tests.MockLel import MockLel



class VerbosView(APIView):
    def get(self, request):
        lelMockeado = MockLel().lelMockeadoHospital()
        diagrama = Diagrama([], [])

        aplicadorDeReglasVerbo = AplicadorDeReglasVerbo(diagrama) 
        lelsCategoricosDeVerbo = aplicadorDeReglasVerbo.aplicarReglasDeVerbo(lelMockeado)

        aplicadorDeReglasSujeto = AplicadorDeReglasSujeto(diagrama)
        aplicadorDeReglasSujeto.aplicarReglasDeSujeto(lelsCategoricosDeVerbo, lelMockeado)

        return Response(diagrama)

    
       
