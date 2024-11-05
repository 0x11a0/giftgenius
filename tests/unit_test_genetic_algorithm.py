import sys
import os
import unittest
import random

# Ensure reproducibility of results
random.seed(42)

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import required modules
from core.models.product import Product
from algorithms.genetic import genetic_algorithm

class TestGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        # Sample products list for testing
        self.products = [
            Product(name="Wireless Earbuds", category="Electronics", price=50, base_satisfaction=80, tags=["Tech", "Earbuds", "Wireless"], synergy_items=["Phone Charger"]),
            Product(name="Phone Charger", category="Electronics", price=20, base_satisfaction=60, tags=["Tech", "Charger", "Portable"], synergy_items=["Wireless Earbuds"]),
            Product(name="Screwdriver Set", category="Home Improvement", price=15, base_satisfaction=50, tags=["Tools", "Screwdriver"], synergy_items=["Cordless Drill"]),
            Product(name="Cordless Drill", category="Home Improvement", price=60, base_satisfaction=85, tags=["Tools", "Power Drill", "Cordless"], synergy_items=["Screwdriver Set"]),
            Product(name="Bluetooth Speaker", category="Electronics", price=40, base_satisfaction=70, tags=["Music", "Speaker", "Wireless"], synergy_items=["Phone Charger"]),
        ]
        self.user_tags = ["Tech Lover", "Music Enthusiast"]

    def test_genetic_algorithm_with_sufficient_budget(self):
        # Test the algorithm with a budget that allows multiple items
        budget = 100
        best_bundle, best_satisfaction = genetic_algorithm(self.products, self.user_tags, budget)

        # Assert the budget constraint is respected
        total_cost = sum(product.price for product in best_bundle)
        self.assertLessEqual(total_cost, budget, "Total cost exceeds budget.")

        # Assert that we get a non-zero satisfaction score
        self.assertGreater(best_satisfaction, 0, "Expected a positive satisfaction score.")

        # Print results for verification
        print("\nTest Output - Genetic Algorithm with Sufficient Budget")
        for product in best_bundle:
            print(f"- {product.name} (${product.price}) - Satisfaction: {product.base_satisfaction}")
        print(f"Total Satisfaction Score: {best_satisfaction}")
        print(f"Total Cost: {total_cost}\n")

    def test_genetic_algorithm_with_low_budget(self):
        # Test the algorithm with a very low budget that can only afford one item
        budget = 30
        best_bundle, best_satisfaction = genetic_algorithm(self.products, self.user_tags, budget)

        # Assert the budget constraint is respected
        total_cost = sum(product.price for product in best_bundle)
        self.assertLessEqual(total_cost, budget, "Total cost exceeds budget.")

        # Assert that we get a non-zero satisfaction score and only one item selected
        self.assertGreater(best_satisfaction, 0, "Expected a positive satisfaction score.")
        self.assertEqual(len(best_bundle), 1, "Expected only one item in the bundle due to low budget.")

        # Print results for verification
        print("\nTest Output - Genetic Algorithm with Low Budget")
        for product in best_bundle:
            print(f"- {product.name} (${product.price}) - Satisfaction: {product.base_satisfaction}")
        print(f"Total Satisfaction Score: {best_satisfaction}")
        print(f"Total Cost: {total_cost}\n")

    def test_genetic_algorithm_with_high_budget(self):
        # Test the algorithm with a high budget that can cover all items
        budget = 200
        best_bundle, best_satisfaction = genetic_algorithm(self.products, self.user_tags, budget)

        # Assert the budget constraint is respected
        total_cost = sum(product.price for product in best_bundle)
        self.assertLessEqual(total_cost, budget, "Total cost exceeds budget.")

        # Assert that we get a high satisfaction score
        self.assertGreater(best_satisfaction, 200, "Expected a higher satisfaction score with high budget.")

        # Print results for verification
        print("\nTest Output - Genetic Algorithm with High Budget")
        for product in best_bundle:
            print(f"- {product.name} (${product.price}) - Satisfaction: {product.base_satisfaction}")
        print(f"Total Satisfaction Score: {best_satisfaction}")
        print(f"Total Cost: {total_cost}\n")

if __name__ == "__main__":
    unittest.main()
