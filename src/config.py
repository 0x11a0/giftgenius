import os
from dotenv import load_dotenv

# Load environment variables from a .env file if available
load_dotenv()

class Config:
    # Database Paths    
    PRODUCTS_FILE="data/products.json"
    PROFILES_FILE="data/profiles.json"

    # OpenAI API Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_default_openai_api_key_here")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default model for tag generation

    # Budget and Algorithm Parameters
    DEFAULT_BUDGET = int(os.getenv("DEFAULT_BUDGET", "100"))  # Default budget if not specified
    MAX_TAG_TOKENS = int(os.getenv("MAX_TAG_TOKENS", "50"))   # Max tokens for tag generation
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))       # Temperature for randomness in tag generation

    # File Paths
    PRODUCTS_FILE = os.getenv("PRODUCTS_FILE", "data/products.json")
    PROFILES_FILE = os.getenv("PROFILES_FILE", "data/profiles.json")

    # Simulated Annealing Parameters
    INITIAL_TEMPERATURE = float(os.getenv("INITIAL_TEMPERATURE", "1000"))
    COOLING_RATE = float(os.getenv("COOLING_RATE", "0.95"))
    MIN_TEMPERATURE = float(os.getenv("MIN_TEMPERATURE", "1"))

    # Genetic Algorithm Parameters
    POPULATION_SIZE = int(os.getenv("POPULATION_SIZE", "10"))
    GENERATIONS = int(os.getenv("GENERATIONS", "50"))
    MUTATION_RATE = float(os.getenv("MUTATION_RATE", "0.1"))
    SELECTION_SIZE = int(os.getenv("SELECTION_SIZE", "5"))

    # Relevance Points Configuration
    EXACT_MATCH_POINTS = int(os.getenv("EXACT_MATCH_POINTS", "10"))
    PARTIAL_MATCH_POINTS = int(os.getenv("PARTIAL_MATCH_POINTS", "5"))

    # Synergy Points Configuration
    SYNERGY_POINTS_PER_PAIR = int(os.getenv("SYNERGY_POINTS_PER_PAIR", "15"))

# Initialize the config
config = Config()
