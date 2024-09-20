from rest_framework import viewsets
from Student. models import Record
from .serializer import RecordSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer