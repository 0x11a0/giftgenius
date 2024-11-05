import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from core.models.product import Product
from core.relevance.calculate_relevance import calculate_relevance_points, calculate_personalized_satisfaction

# Sample data
user_tags = ["Tech Enthusiast", "Music Lover", "Outdoorsy"]
product = Product(
    name="Wireless Earbuds",
    category="Electronics",
    price=50,
    base_satisfaction=80,
    tags=["Tech", "Earbuds", "Wireless"],
    synergy_items=["Phone Charger"]
)

# Calculate relevance points
relevance_points = calculate_relevance_points(user_tags, product.tags)

# Calculate personalized satisfaction
personalized_satisfaction = calculate_personalized_satisfaction(product, relevance_points)

print(f"Relevance Points: {relevance_points}")
print(f"Personalized Satisfaction: {personalized_satisfaction}")
