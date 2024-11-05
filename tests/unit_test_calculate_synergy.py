import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now you can import the Product class and calculate_synergy function
from core.models.product import Product
from core.synergy.calculate_synergy import calculate_synergy

# Sample selected products for testing
selected_products = [
    Product(name="Wireless Earbuds", category="Electronics", price=50, base_satisfaction=80, 
            tags=["Tech", "Earbuds", "Wireless"], synergy_items=["Phone Charger"]),
    Product(name="Phone Charger", category="Electronics", price=20, base_satisfaction=60, 
            tags=["Tech", "Charger", "Portable"], synergy_items=["Wireless Earbuds"]),
    Product(name="Screwdriver Set", category="Home Improvement", price=15, base_satisfaction=50, 
            tags=["Tools", "Screwdriver"], synergy_items=["Cordless Drill"]),
    Product(name="Cordless Drill", category="Home Improvement", price=60, base_satisfaction=85, 
            tags=["Tools", "Power Drill", "Cordless"], synergy_items=["Screwdriver Set"])
]

# Calculate synergy points for the selected products
synergy_points = calculate_synergy(selected_products)
print(f"Total Synergy Points: {synergy_points}")
