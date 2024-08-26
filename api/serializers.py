from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    address=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance ,validated_data):
        instance.name=validated_data.get('name', instance.name)    
        instance.address=validated_data.get('address', instance.address)
        instance.save()
        return instance
    

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
