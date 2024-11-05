from config import config

# Define the synergy points awarded for each complementary pair
SYNERGY_POINTS_PER_PAIR=config.SYNERGY_POINTS_PER_PAIR

def calculate_synergy(selected_products):
    """
    Calculates the total synergy points for a list of selected products.
    :param selected_products: List of Product objects in the selected gift bundle.
    :return: Total synergy points.
    """

    total_synergy_points = 0

    # Iterate through each unique pair of products in the bundle
    for i in range(len(selected_products)):
        for j in range(i + 1, len(selected_products)):
            product_a = selected_products[i]
            product_b = selected_products[j]

            # Check if product_b is in product_a's synergy items or vice versa
            if product_b.name in product_a.synergy_items or product_a.name in product_b.synergy_items:
                total_synergy_points += SYNERGY_POINTS_PER_PAIR

    return total_synergy_points
