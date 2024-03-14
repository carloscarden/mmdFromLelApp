from rest_framework import serializers

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['nombre', 'edad']
