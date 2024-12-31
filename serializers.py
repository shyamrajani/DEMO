from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        field = '__all__'

    def validate(self ,data):
        if data['age']<18:
            raise serializers.ValidationError({'error':"age cannot be less then 18"})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':"name cannot be in numeric "})
                

        return data
    
class CategroySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categroy
        field = '__all__'

class BookSerializer(serializers.ModelSerializer):
    categroy = CategroySerializer()
    class Meta:
        model = Book
        field = '__all__'