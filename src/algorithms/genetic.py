import random
from core.models.product import Product
from core.relevance.calculate_relevance import calculate_relevance_points, calculate_personalized_satisfaction
from algorithms.greedy import generate_initial_gift_bundle
from config import config  # Import configuration settings

# Genetic Algorithm Parameters from config
POPULATION_SIZE = config.POPULATION_SIZE
GENERATIONS = config.GENERATIONS
MUTATION_RATE = config.MUTATION_RATE
SELECTION_SIZE = config.SELECTION_SIZE

def fitness(bundle, budget):
    """
    Calculate the fitness of a gift bundle based on total satisfaction and budget constraints.
    :param bundle: List of Product objects.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: Fitness score (total satisfaction) if within budget, otherwise 0.
    """
    total_cost = sum(product.price for product in bundle)
    if total_cost > budget:
        return 0
    total_satisfaction = sum(product.base_satisfaction for product in bundle)
    return total_satisfaction

def generate_initial_population(products, user_tags, budget):
    """
    Generate the initial population for the Genetic Algorithm.
    :param products: List of Product objects.
    :param user_tags: List of tags representing the recipient's interests.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: List of bundles (each bundle is a list of Product objects).
    """
    population = []
    for _ in range(POPULATION_SIZE):
        bundle = []
        remaining_budget = budget
        random.shuffle(products)  # Shuffle to create diversity in bundles
        for product in products:
            if product.price <= remaining_budget:
                relevance_points = calculate_relevance_points(user_tags, product.tags)
                personalized_satisfaction = calculate_personalized_satisfaction(product, relevance_points)
                product.personalized_satisfaction = personalized_satisfaction
                bundle.append(product)
                remaining_budget -= product.price
        population.append(bundle)
    return population

def generate_initial_population_with_greedy(products, user_tags, budget):
    """
    Generate the initial population using the Greedy Algorithm for higher-quality starting bundles.
    :param products: List of Product objects.
    :param user_tags: List of tags representing the recipient's interests.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: List of bundles (each bundle is a list of Product objects).
    """
    population = []
    for _ in range(POPULATION_SIZE):
        # Shuffle products to introduce variation for each greedy run
        random.shuffle(products)
        # Generate a bundle using the Greedy Algorithm
        bundle, _ = generate_initial_gift_bundle(products, user_tags, budget)
        population.append(bundle)
    return population

def select_parents(population, budget):
    """
    Select parents for crossover based on fitness scores.
    :param population: List of bundles.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: Selected parent bundles for crossover.
    """
    # Calculate fitness for each bundle
    fitness_scores = [(bundle, fitness(bundle, budget)) for bundle in population]
    # Sort by fitness in descending order
    fitness_scores.sort(key=lambda x: x[1], reverse=True)
    # Select top bundles as parents
    parents = [bundle for bundle, _ in fitness_scores[:SELECTION_SIZE]]
    return parents

def crossover(parent1, parent2, budget):
    """
    Perform crossover between two parent bundles to produce an offspring.
    :param parent1: First parent bundle.
    :param parent2: Second parent bundle.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: Offspring bundle.
    """
    # Crossover: randomly choose items from each parent until budget is reached
    offspring = []
    remaining_budget = budget
    combined_products = parent1 + parent2
    random.shuffle(combined_products)
    
    for product in combined_products:
        if product.price <= remaining_budget and product not in offspring:
            offspring.append(product)
            remaining_budget -= product.price
    return offspring

def mutate(bundle, products, budget):
    """
    Apply mutation to a bundle by randomly swapping products.
    :param bundle: Bundle to mutate.
    :param products: List of all available products.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: Mutated bundle.
    """
    if random.random() < MUTATION_RATE:
        # Randomly select a product to remove and a new product to add
        product_to_remove = random.choice(bundle)
        bundle.remove(product_to_remove)
        remaining_budget = budget - sum(product.price for product in bundle)
        
        # Try to add a random new product within the remaining budget
        available_products = [p for p in products if p.price <= remaining_budget and p not in bundle]
        if available_products:
            bundle.append(random.choice(available_products))
    return bundle

def genetic_algorithm(population, products, user_tags, budget):
    """
    Run the Genetic Algorithm to find an optimal gift bundle.
    :param products: List of Product objects.
    :param user_tags: List of tags representing the recipient's interests.
    :param budget: Maximum allowable spending for the gift bundle.
    :return: Best bundle found by the algorithm and its satisfaction score.
    """

    for generation in range(GENERATIONS):
        new_population = []
        parents = select_parents(population, budget)

        # Crossover and create new population
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(parents, 2)
            offspring = crossover(parent1, parent2, budget)
            offspring = mutate(offspring, products, budget)
            new_population.append(offspring)
        
        population = new_population

    # Get the best bundle from the final population
    best_bundle = max(population, key=lambda bundle: fitness(bundle, budget))
    best_satisfaction = fitness(best_bundle, budget)

    return best_bundle, best_satisfaction
