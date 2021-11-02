import pandas as pd

from datetime import datetime, timezone
from django.shortcuts import render

from cadastro.models import Cadastro


def simple_upload(request):
    if request.method == 'POST':
        arquivo = request.FILES['arquivo']
        nome_arquivo = str(arquivo)
        if nome_arquivo.endswith(".xlsx"):
            data = pd.read_excel(arquivo.read())
            data.sort_values(by=['id'], inplace=True, ignore_index=True)

            cont = 0
            for cont in range(len(data)):
                nome = data["nome"][cont]
                sobrenome = data["sobrenome"][cont]
                sexo = data["sexo"][cont]
                altura = data["altura"][cont]
                peso = data["peso"][cont]
                nascimento = datetime.fromtimestamp(data["nascimento"][cont], tz=timezone.utc)
                bairro = data["bairro"][cont]
                cidade = data["cidade"][cont]
                estado = data["estado"][cont]
                numero = data["numero"][cont]
                cont += 1
                Cadastro.objects.create(
                    nome=nome,
                    sobrenome=sobrenome,
                    sexo=sexo,
                    altura=altura,
                    peso=peso,
                    nascimento=nascimento,
                    bairro=bairro,
                    cidade=cidade,
                    estado=estado,
                    numero=numero,
                )

    return render(request, 'import.html')


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
