from rest_framework import serializers
from ss.models import Emp

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'

    def create(self, validated_data):
        return Emp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.movie_name)
        instance.age = validated_data.get('age', instance.language)
        instance.save()
        return instance




