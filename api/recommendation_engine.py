# api/recommendation_engine.py

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

def collaborative_filtering(user_id, interactions):
    """
    Collaborative Filtering: Recommends products based on user interaction similarity.
    """
    user_product_matrix = defaultdict(lambda: defaultdict(int))

    # Populate interaction matrix
    for interaction in interactions:
        user_product_matrix[interaction["user_id"]][interaction["product_id"]] += 1

    # Build product-user interaction matrix
    users = list(user_product_matrix.keys())
    products = set(
        product for user_interactions in user_product_matrix.values() for product in user_interactions
    )
    user_index = {user: idx for idx, user in enumerate(users)}
    product_index = {product: idx for idx, product in enumerate(products)}

    interaction_matrix = np.zeros((len(users), len(products)))
    for user, product_interactions in user_product_matrix.items():
        for product, count in product_interactions.items():
            interaction_matrix[user_index[user], product_index[product]] = count

    # Compute similarity
    if user_id not in user_index:
        return []  # No recommendations for new users
    user_vector = interaction_matrix[user_index[user_id]].reshape(1, -1)
    similarities = cosine_similarity(interaction_matrix, user_vector).flatten()
    similar_users_idx = np.argsort(-similarities)[1:6]  # Top 5 similar users

    # Aggregate recommendations
    recommended_products = set()
    for similar_user_idx in similar_users_idx:
        similar_user_id = users[similar_user_idx]
        recommended_products.update(user_product_matrix[similar_user_id].keys())

    return list(recommended_products - set(user_product_matrix[user_id].keys()))  # Exclude already interacted


def content_based_filtering(user_id, products, interactions):
    """
    Content-Based Filtering: Recommends products based on product feature similarity.
    """
    # Build product feature matrix
    product_ids = [product["product_id"] for product in products]
    product_features = np.array([list(product["features"].values()) for product in products])

    # Compute product similarity
    similarity_matrix = cosine_similarity(product_features)

    # Get user interaction data
    user_interactions = [interaction["product_id"] for interaction in interactions if interaction["user_id"] == user_id]

    # Aggregate recommendations
    recommended_products = set()
    for product_id in user_interactions:
        if product_id in product_ids:
            product_idx = product_ids.index(product_id)
            similar_product_idxs = np.argsort(-similarity_matrix[product_idx])[:5]  # Top 5 similar products
            recommended_products.update(product_ids[idx] for idx in similar_product_idxs)

    return list(recommended_products - set(user_interactions))  # Exclude already interacted


def recommend(user_id, strategy="collaborative", products=None, interactions=None):
    """
    Unified function to recommend products using different strategies.
    """
    if strategy == "collaborative":
        return collaborative_filtering(user_id, interactions or [])
    elif strategy == "content":
        return content_based_filtering(user_id, products or [], interactions or [])
    return []
