from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from api.serializers.serializer import CourtSerializer
from api.models import CourtDecision

class AllCourtDecision(APIView):
    """
    Returns the view content for general court decisions

    Methods:
        GET - All content ordered by `id_cliente`
        POST - Insert one entry into DB
        PUT - Update partially the selected row based on `id`
        DELETE - Remove selected row based on `id`
    """
    def get(self, request):
        queryset = CourtDecision.objects.all().order_by('id_cliente')
        serializer = CourtSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        decision = CourtDecision.objects.get(id=kwargs['id'])
        serializer = CourtSerializer(decision, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        decision = CourtDecision.objects.get(id=kwargs['id'])
        decision.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CountClientCourtDecisions(APIView):
    """
    Returns the sum of each type of decision for the client, the sum is made
    with list comprehension based on the three types of options available.

    0 - Against the client
    1 - Partially to the client
    2 - In favor of the client

    Methods:
        GET - Returns a dict with the sum of how many times the client
        got a favored (or not) decision`
    """
    def get(self, request, **kwargs):
        queryset = CourtDecision.objects.filter(id_cliente=kwargs['id_cliente'])
        serializer = CourtSerializer(queryset, many=True)
        
        court_favor_decision = {
            'negative': sum(1 for eachDictSerializer in serializer.data if \
                eachDictSerializer.get('favor_contribuinte') == str(0)),
            'parcial': sum(1 for eachDictSerializer in serializer.data if \
                eachDictSerializer.get('favor_contribuinte') == str(1)),
            'positive': sum(1 for eachDictSerializer in serializer.data if \
                eachDictSerializer.get('favor_contribuinte') == str(2))
            }
        return Response(court_favor_decision)

class ClientCourtDecisions(APIView):
    """
    Returns all client decisions recorded

    Method:
        GET - Return a list of dicts with the decisions informations
    """
    def get(self, request, **kwargs):
        queryset = CourtDecision.objects.filter(id_cliente=kwargs['id_cliente'])
        serializer = CourtSerializer(queryset, many=True)

        return Response(serializer.data)