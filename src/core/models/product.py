class Product:
    def __init__(self, name, category, price, base_satisfaction, tags, synergy_items):
        """
        Initializes a Product object.
        :param name: Name of the product.
        :param category: Category of the product (e.g., Electronics, Home Improvement).
        :param price: Price of the product.
        :param base_satisfaction: Base satisfaction score for the product.
        :param tags: List of tags describing the product's attributes.
        :param synergy_items: List of product names that synergize with this product.
        """
        self.name = name
        self.category = category
        self.price = price
        self.base_satisfaction = base_satisfaction
        self.tags = tags
        self.synergy_items = synergy_items

    def __repr__(self):
        """
        Provides a string representation of the Product object for easier debugging.
        :return: String representation of the product.
        """
        return f"Product(name={self.name}, category={self.category}, price={self.price}, base_satisfaction={self.base_satisfaction})"
