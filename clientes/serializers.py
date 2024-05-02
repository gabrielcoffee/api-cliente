from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "CPF inválido"})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números nesse campo"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "Rg deve conter 9 digitos"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "Celular deve ter formato válido(99 91234-1234)"})
        
        return data