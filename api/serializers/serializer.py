from rest_framework import serializers
from api.models import CourtDecision

class CourtSerializer(serializers.HyperlinkedModelSerializer):
    """
    Model serialization of the CourtDecisions, to be able to serialize
    and deserialize the instances in a better format for working.
    """
    class Meta:
        model = CourtDecision
        fields = ('id', 'n_processo', 'ementa', 'favor_contribuinte', 'id_cliente')