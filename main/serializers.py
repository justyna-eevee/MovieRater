from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, ExtraInfo

class ExtraInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['time', 'rodzaj']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    info = ExtraInfoSerializer(many=False)
    class Meta:
        model = Movie
        fields = ['id', 'name', 'year', 'description', 'released', 'info']

