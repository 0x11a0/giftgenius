import random
import math
from algorithms.genetic import genetic_algorithm, mutate, fitness
from core.models.product import Product
from config import config  # Import the configuration

# Simulated Annealing Parameters
INITIAL_TEMPERATURE = config.INITIAL_TEMPERATURE
COOLING_RATE = config.COOLING_RATE
MIN_TEMPERATURE = config.MIN_TEMPERATURE

def simulated_annealing(bundle, products, budget):
    """
    Perform simulated annealing on a gift bundle to improve satisfaction within budget.
    :param bundle: Initial bundle from the Genetic Algorithm.
    :param products: List of all available products.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: Optimized bundle and satisfaction score.
    """
    current_bundle = bundle[:]
    current_satisfaction = fitness(current_bundle, budget)
    temperature = INITIAL_TEMPERATURE

    while temperature > MIN_TEMPERATURE:
        # Generate a neighboring bundle by mutating the current bundle
        new_bundle = mutate(current_bundle, products, budget)
        new_satisfaction = fitness(new_bundle, budget)

        # Calculate the acceptance probability
        delta_satisfaction = new_satisfaction - current_satisfaction
        if delta_satisfaction > 0 or math.exp(delta_satisfaction / temperature) > random.random():
            # Accept the new bundle
            current_bundle = new_bundle
            current_satisfaction = new_satisfaction

        # Cool down the temperature
        temperature *= COOLING_RATE

    return current_bundle, current_satisfaction

def genetic_algorithm_with_annealing(products, user_tags, budget):
    """
    Use the Genetic Algorithm to find an initial solution, then refine with Simulated Annealing.
    :param products: List of Product objects.
    :param user_tags: List of tags representing the recipient's interests.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: Optimized bundle and satisfaction score.
    """
    # Step 1: Use the Genetic Algorithm to find a good initial solution
    initial_bundle, initial_satisfaction = genetic_algorithm(products, user_tags, budget)

    # Step 2: Refine the initial solution using Simulated Annealing
    optimized_bundle, optimized_satisfaction = simulated_annealing(initial_bundle, products, budget)

    return optimized_bundle, optimized_satisfaction
