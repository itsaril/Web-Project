from django.shortcuts import render
from django.http.response import JsonResponse

from api.models import Company, Game
from api.serializers import CompanySerializer, GameSerializer

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create your views here.
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)

def company_details(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    serializer = CompanySerializer(company)

    return JsonResponse(serializer.data, safe=False ,status=200)

def company_games(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    games = Game.objects.filter(company=company)
    serializer = GameSerializer(games, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)

def Game_list(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)

def Game_details(request, id):
    try:
        Game = Game.objects.get(id=id)
    except Game.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    serializer = GameSerializer(Game)

    return JsonResponse(serializer.data, safe=False, status=200)

def Game_top_ten(request):
    games = Game.objects.order_by('-salary')[:10]
    serializer = GameSerializer(games, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)

class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass