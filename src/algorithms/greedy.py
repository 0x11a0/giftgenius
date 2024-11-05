import json
from core.models.product import Product
from core.relevance.calculate_relevance import calculate_relevance_points, calculate_personalized_satisfaction

def generate_initial_gift_bundle(products, user_tags, budget):
    """
    Generates an initial gift bundle using the Greedy Algorithm.
    :param products: List of Product objects.
    :param user_tags: List of tags representing the recipient's interests.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: List of selected Product objects and total satisfaction score.
    """
    # Calculate personalized satisfaction and value per dollar for each product
    personalized_products = []
    for product in products:
        relevance_points = calculate_relevance_points(user_tags, product.tags)
        personalized_satisfaction = calculate_personalized_satisfaction(product, relevance_points)
        value_per_dollar = personalized_satisfaction / product.price
        personalized_products.append((product, personalized_satisfaction, value_per_dollar))

    # Sort products by value per dollar in descending order
    personalized_products.sort(key=lambda x: x[2], reverse=True)

    # Select products based on value per dollar until budget is exhausted
    selected_products = []
    total_satisfaction = 0
    remaining_budget = budget

    for product, satisfaction, _ in personalized_products:
        if product.price <= remaining_budget:
            selected_products.append(product)
            total_satisfaction += satisfaction
            remaining_budget -= product.price

    return selected_products, total_satisfaction
