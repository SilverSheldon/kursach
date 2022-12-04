import collections

from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Statistics
from api.serializers import StatisticsSerializer
from drf_spectacular.utils import extend_schema


class StatisticsView(APIView):
    @extend_schema(request=StatisticsSerializer, responses=StatisticsSerializer)
    def get(self, request, s):
        stat = Statistics(s=s, symbol_count=collections.Counter(s), str_len=len(s))
        print(StatisticsSerializer(instance=stat).data)
        return Response(StatisticsSerializer(instance=stat).data)
