import json
import os
from config import config

def load_json(filepath):
    """
    Loads JSON data from a file.
    :param filepath: Path to the JSON file.
    :return: Parsed JSON data as a Python object, or an empty list if file not found.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []

def calculate_total_cost(bundle):
    """
    Calculates the total cost of products in a bundle.
    :param bundle: List of Product objects.
    :return: Total cost as a float.
    """
    return sum(product.price for product in bundle)

def calculate_total_satisfaction(bundle):
    """
    Calculates the total satisfaction score of products in a bundle.
    :param bundle: List of Product objects.
    :return: Total satisfaction score as an integer.
    """
    return sum(product.calculate_personalized_satisfaction() for product in bundle)

def within_budget(bundle, budget=config.DEFAULT_BUDGET):
    """
    Checks if the total cost of a bundle is within the specified budget.
    :param bundle: List of Product objects.
    :param budget: Maximum allowable budget.
    :return: Boolean indicating if the bundle is within budget.
    """
    return calculate_total_cost(bundle) <= budget

def format_bundle(bundle):
    """
    Formats the bundle information for display.
    :param bundle: List of Product objects.
    :return: Formatted string containing details of each product in the bundle.
    """
    formatted_bundle = []
    for product in bundle:
        formatted_bundle.append(f"{product.name} - ${product.price} (Satisfaction: {product.base_satisfaction})")
    return "\n".join(formatted_bundle)

def format_bundles(bundle):
    """
    Formats the bundle information for display.
    :param bundle: List of Product objects.
    :return: Formatted string containing details of each product in the bundle.
    """
    formatted_bundles = []
    for bundle in bundles:
        for product in bundle:
            formatted_bundles.append(f"{product.name} - ${product.price} (Satisfaction: {product.base_satisfaction})")
    return "\n".join(formatted_bundles)

def load_products():
    """
    Loads the product catalog from the JSON file specified in the config.
    :return: List of product data loaded from JSON.
    """
    return load_json(config.PRODUCTS_FILE)

def load_profiles():
    """
    Loads recipient profiles from the JSON file specified in the config.
    :return: List of recipient profile data loaded from JSON.
    """
    return load_json(config.PROFILES_FILE)
