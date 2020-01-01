from django.contrib.auth.models import User, Group
from rest_framework import serializers

from QuiGolaco.api.models import Jogadores


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class JogadoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jogadores
        fields = ['nome', 'idade', 'altura', 'num_gols', 'num_assistencias']