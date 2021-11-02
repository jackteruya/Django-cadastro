from rest_framework import serializers

from cadastro.models import Cadastro


class CadastroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cadastro
        fields = [
            'id',
            'nome',
            'sobrenome',
            'sexo',
            'altura',
            'peso',
            'nascimento',
            'bairro',
            'cidade',
            'estado',
            'numero',
        ]
