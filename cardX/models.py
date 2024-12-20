import jsonfield
from django.db import models
from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination


# Create your models here.

class MdCard(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)  # MongoDB的_id字段通常作为主键
    attack = models.CharField(max_length=50)
    attribute = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    ch_name = models.CharField(max_length=200)
    defence = models.CharField(max_length=50)
    desc = models.TextField()
    eng_name = models.CharField(max_length=200)
    img_url = models.URLField()
    jp_name = models.CharField(max_length=200)
    race = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)
    stars = models.IntegerField()

    class Meta:
        db_table = 'md'  # 指定对应的MongoDB集合名称

    def __str__(self):
        return self.ch_name

class PokemonCard(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)  # MongoDB的_id字段通常作为主键
    ability_effect = models.TextField()
    ability_info = models.CharField(max_length=255)
    attacks = jsonfield.JSONField()  # 使用JSONField存储攻击信息
    card_number = models.CharField(max_length=50)
    evolves_link = models.CharField(max_length=255)
    hp = models.IntegerField()
    illustrator = models.CharField(max_length=255)
    image_url = models.URLField()
    name = models.CharField(max_length=255)
    resistance = models.CharField(max_length=50)
    retreat_cost = models.CharField(max_length=10)  # 退却费用可能包含非数字字符，所以用CharField
    type = models.CharField(max_length=50)
    weakness = models.CharField(max_length=50)

    class Meta:
        db_table = 'pokemoncards'  # 指定对应的MongoDB集合名称

    def __str__(self):
        return self.name



class TrainerCard(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)  # MongoDB的_id字段通常作为主键
    card_ability = models.TextField()
    card_number = models.CharField(max_length=50)
    illustrator = models.CharField(max_length=255)
    image_url = models.URLField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)

    class Meta:
        db_table = 'trainercards'  # 指定对应的MongoDB集合名称


    def __str__(self):
        return self.name


# ModelSerializer 序列化器
class TrainerCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerCard
        fields = '__all__'

class MdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MdCard
        fields = '__all__'


class PokemonCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonCard
        fields = '__all__'