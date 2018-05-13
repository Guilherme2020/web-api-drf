from datetime import date
from django.db.models import Exists
from rest_framework import serializers, request
from rest_framework.decorators import api_view
from rest_framework.fields import SlugField
from rest_framework.validators import UniqueValidator
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','release_date','game_category')

    #1 questao, campos vazios

    def field_valid(self, field):
        print(field, type(field))
        if field is None or field == "":
            raise serializers.ValidationError("Campo Vazio, por favor preencha todos os campos")

        return field

    def validate_name(self,name):

        game = Game.objects.filter(name=name).exists()

        if game:
            raise serializers.ValidationError('Nome ja existente, favor escolher outro nome de jogo')
        return self.field_valid(name)

    def validate_release_date(self,release_date):

        if release_date  < date.today():
            raise serializers.ValidationError('Jogo ainda não lançado. Exclusão não  permitida. ')

        return self.field_valid(release_date)

    def validate_game_category(self,game_category):
        return self.field_valid(game_category)

