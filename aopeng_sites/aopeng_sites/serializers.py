from django.contrib.auth.models import User, Group
from rest_framework import serializers
from op_xadmin.models import goods


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class goodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = goods
        fields = ('op_id', 'kayouli_id', 'factory_name', 'goods_name', 'color', 'size', 'normal_size_price', 'big_size_price')


