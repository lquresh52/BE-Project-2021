from rest_framework import serializers
from adminPanel.models import *



class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

