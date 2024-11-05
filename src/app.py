from core.profile_generation.tag_generator import generate_tags
from algorithms.genetic import genetic_algorithm, generate_initial_population_with_greedy
from algorithms.simulated_annealing import simulated_annealing
from core.relevance.calculate_relevance import calculate_relevance_points, calculate_personalized_satisfaction
from core.synergy.calculate_synergy import calculate_synergy
from core.models.product import Product
from utils.helpers import load_products, load_profiles, format_bundle, within_budget
from utils.logger import get_logger

# Set up the logger
logger = get_logger(__name__)

def main():
    # Step 1: Gather User Input
    recipient_description = input("Enter a description of the recipient: ")
    budget = float(input("Enter the budget for the gift bundle: "))
    
    # Step 2: Generate Interest Tags from Recipient Description
    logger.info("Generating tags based on recipient description.")
    tags = generate_tags(recipient_description)
    logger.info(f"Generated tags: {tags}")
    
    # Step 3: Load Products from Data
    logger.info("Loading products from catalog.")
    products_data = load_products()
    products = []
    
    # Step 4: Calculate Relevance and Satisfaction for Products
    logger.info("Calculating relevance and personalized satisfaction for each product.")
    for product_data in products_data:
        # Create a Product instance from each product data dictionary
        product = Product(
            name=product_data['name'],
            category=product_data['category'],
            price=product_data['price'],
            base_satisfaction=product_data['base_satisfaction'],
            tags=product_data['tags'],
            synergy_items=product_data['synergy_items']
        )
        
        # Calculate relevance points and personalized satisfaction
        relevance_points = calculate_relevance_points(tags, product.tags)
        product.personalized_satisfaction = calculate_personalized_satisfaction(product, relevance_points)
        
        # Add the product to the list
        products.append(product)
    
    # Step 5: Generate Initial Bundle with Greedy Algorithm
    logger.info("Generating initial gift bundle using Greedy Algorithm.")
    initial_bundles, _ = generate_initial_population_with_greedy(products, tags, budget)
    logger.info(f"Initial bundle: {format_bundles(initial_bundle)}")
    
    # Step 6: Refine Bundle with Genetic Algorithm + Simulated Annealing
    logger.info("Refining bundle with Genetic Algorithm.")
    refined_bundles, _ = genetic_algorithm(initial_bundles, products, tags, budget)
    logger.info(f"Refined bundle after Genetic Algorithm: {format_bundle(refined_bundle)}")
    
    # Step 7: Final Optimization with Simulated Annealing
    logger.info("Final optimization using Simulated Annealing.")
    optimized_bundle, _ = simulated_annealing(refined_bundles, products, budget)
    logger.info(f"Optimized bundle after Simulated Annealing: {format_bundle(optimized_bundle)}")
    
    # Step 8: Display Final Gift Bundle with Synergy Score
    logger.info("Calculating final synergy points for the optimized bundle.")
    total_synergy = calculate_synergy(optimized_bundle)
    total_cost = sum(product.price for product in optimized_bundle)
    total_satisfaction = sum(product.personalized_satisfaction for product in optimized_bundle) + total_synergy

    print("\nFinal Gift Bundle:")
    print(format_bundle(optimized_bundle))
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Total Satisfaction Score: {total_satisfaction}")
    print(f"Total Synergy Points: {total_synergy}")
    print("\nThank you for using GiftGenius!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
