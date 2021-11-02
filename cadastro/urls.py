from django.urls import path

from cadastro.api_views import ListarMulheresDeMereenAPIView, ListarCadastrAPIView
from cadastro.views import simple_upload, home


urlpatterns = [
    # API
    path('listar-mulheres-meeren/', ListarMulheresDeMereenAPIView.as_view(), name='listar-mulheres-mereen'),
    path('cadastro/<str:sexo>/', ListarCadastrAPIView.as_view(), name='cadastro'),

    # url para fazer upload do arquivo xlsx
    path('dados-upload/', simple_upload),
    path('', home),
]
