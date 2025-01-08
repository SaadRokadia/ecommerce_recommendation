from django.urls import path
from .views import get_recommendations, add_interaction

urlpatterns = [
    path('recommendations/<str:user_id>/', get_recommendations, name='get_recommendations'),
    path('interactions/', add_interaction, name='add_interaction'),
]