from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Interaction, Product, User
from .recommendation_engine import recommend
import json

@csrf_exempt
def get_recommendations(request, user_id):
    strategy = request.GET.get('strategy', 'collaborative')
    interactions = list(Interaction.objects.values('user_id', 'product_id', 'interaction_type'))
    products = list(Product.objects.values('product_id', 'name', 'features'))
    recommendations = recommend(user_id, strategy, products, interactions)
    return JsonResponse({"recommendations": recommendations})

@csrf_exempt
def add_interaction(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user, _ = User.objects.get_or_create(user_id=data['user_id'])
        product, _ = Product.objects.get_or_create(product_id=data['product_id'], defaults={"name": "Unknown", "features": {}})
        Interaction.objects.create(
            user=user,
            product=product,
            interaction_type=data['interaction_type']
        )
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid request method"}, status=400)
