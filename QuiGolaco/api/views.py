from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from QuiGolaco.api.models import Jogadores
from QuiGolaco.api.serializers import UserSerializer, GroupSerializer, JogadoresSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JogadoresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Jogadores.objects.all()
    serializer_class = JogadoresSerializer