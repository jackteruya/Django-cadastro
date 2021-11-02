from rest_framework import generics
from rest_framework.filters import OrderingFilter

from cadastro.serializers import CadastroSerializer
from cadastro.models import Cadastro


class ListarMulheresDeMereenAPIView(generics.ListAPIView):
    queryset = Cadastro.objects.filter(cidade="Meeren", sexo='F')
    serializer_class = CadastroSerializer

    def get_queryset(self):
        cidade = "Meeren"
        sexo = "F"
        return Cadastro.objects.filter(cidade=cidade, sexo=sexo)


class ListarCadastrAPIView(generics.ListAPIView):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['nascimento']

    def get_queryset(self):
        sexo = self.kwargs.get('sexo').upper()
        if sexo:
            return self.queryset.filter(sexo=sexo).order_by('-nascimento')
        return



