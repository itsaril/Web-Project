from rest_framework import serializers
from .models import Company, Game

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields =  ['id', 'name', 'description', 'founded', 'financial_information', 'partners_and_investors']

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'name', 'description','genre', 'platforms', 'relase_date','reviews_and_ratings','sales','financial_results', 'company']