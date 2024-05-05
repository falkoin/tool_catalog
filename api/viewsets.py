from api.models import Tool
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets

from api.serializer import ToolSerializer

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.order_by("-date")
    serializer_class = ToolSerializer
    parser_classes = (MultiPartParser, FormParser)
