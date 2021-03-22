from rest_framework import serializers
from FizzBuzz.models import FizzBuzz


class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = '__all__'

