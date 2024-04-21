from django.urls import path
from api import views

urlpatterns = [
    path("companies/", views.company_list),
    path("companies/<int:id>/", views.company_details),
    path("companies/<int:id>/games/", views.company_games),
    path("games/", views.Game_list),
    path("games/<int:id>/", views.Game_details),
    path("games/top_ten/", views.Game_top_ten),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),
]
