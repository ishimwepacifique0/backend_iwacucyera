from . models import *
from rest_framework import serializers
 
class Amatekarializer(serializers.ModelSerializer):
    class Meta :
        model = "Amateka"
        fields = "__all__"

class Diyserializer(serializers.ModelSerializer):
    class Meta :
        model = "Diy"
        fields = "__all__"

class Sakweserializer(serializers.ModelSerializer):
    class Meta :
        model = "Sakwe"
        fields = "__all__"

class Imiganiserializer(serializers.ModelSerializer):
    class Meta :
        model = "Imagani"
        fields = "__all__"


class Herbelserializer(serializers.ModelSerializer):
    class Meta :
        model = "Herbels"
        fields = "__all__"