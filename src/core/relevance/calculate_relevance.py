from config import config

# Relevance points configuration
EXACT_MATCH_POINTS = config.EXACT_MATCH_POINTS
PARTIAL_MATCH_POINTS = config.PARTIAL_MATCH_POINTS

def calculate_relevance_points(user_tags, product_tags):
    """
    Calculates relevance points by comparing user tags with product tags.
    :param user_tags: List of tags representing the user's interests.
    :param product_tags: List of tags associated with the product.
    :return: Integer relevance points.
    """
    relevance_score = 0

    for product_tag in product_tags:
        if product_tag in user_tags:
            relevance_score += EXACT_MATCH_POINTS  # Full points for exact matches
        else:
            # Check for partial match (substring in either direction)
            for user_tag in user_tags:
                if product_tag in user_tag or user_tag in product_tag:
                    relevance_score += PARTIAL_MATCH_POINTS
                    break

    return relevance_score

def calculate_personalized_satisfaction(product, relevance_points):
    """
    Calculates the personalized satisfaction score for a user-product combination.
    :param product: Product object.
    :param relevance_points: Relevance score derived from matching user tags with product tags.
    :return: Integer representing personalized satisfaction score.
    """
    return product.base_satisfaction + relevance_points
