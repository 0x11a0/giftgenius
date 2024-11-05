# TLDR

1. **Tag Extraction**: Use NLP to derive interest tags from the recipient description.
2. **Product Matching**: Calculate relevance and satisfaction scores for each product based on recipient tags.
3. **Bundle Generation**:
   - Start with Greedy Algorithm.
   - Refine using Genetic Algorithm.
   - Fine-tune with Simulated Annealing.
4. **Synergy Calculation**: Calculate synergy points for the final bundle.
5. **Display Bundle**: Present the optimized bundle to the user.


---

### Step 1: User Provides Input

**User Input**:
1. **Recipient Description**: A text description about the recipient (e.g., “A tech-savvy music lover who enjoys outdoor activities”).
2. **Budget**: A maximum spending limit for the gift bundle (e.g., $100).

---

### Step 2: Generate Interest Tags from the Recipient Description

**Process**:
1. The system processes the recipient’s text description using **Natural Language Processing (NLP)** to extract key **interest tags** from the text (e.g., “Tech Lover,” “Music Enthusiast,” “Outdoorsy”).
2. An **AI-based tag generator** creates a list of tags based on keywords and context within the text description. This could involve using pre-trained NLP models or simple keyword matching.

**Example Output**:
- Extracted tags for the recipient: `["Tech Lover", "Music Enthusiast", "Outdoorsy"]`

---

### Step 3: Load Product Data and Prepare for Matching

**Process**:
1. The system loads the product catalog from `products.json`, which contains details about each product (e.g., price, base satisfaction, tags, and synergy items).
2. Each product in the catalog has tags describing its characteristics, which will be used to match products to the recipient’s interests.

**Example Product Data**:
- **Wireless Earbuds**:
  - Tags: `["Tech", "Earbuds", "Wireless"]`
  - Base Satisfaction: `80`
  - Price: `$50`
  - Synergy Items: `["Phone Charger"]`

---

### Step 4: Calculate Relevance Points for Each Product

**Process**:
1. The system calculates **relevance points** for each product based on how well the product’s tags match the recipient’s interest tags.
2. `calculate_relevance_points` compares the tags of each product with the tags of the recipient profile. **Exact matches** receive higher points, while **partial matches** receive lower points.

**Example Calculation**:
- For **Wireless Earbuds**:
  - Recipient Tags: `["Tech Lover", "Music Enthusiast", "Outdoorsy"]`
  - Product Tags: `["Tech", "Earbuds", "Wireless"]`
  - Relevance Points: `20` (assuming two exact matches with "Tech" and "Music")

---

### Step 5: Calculate Personalized Satisfaction for Each Product

**Process**:
1. The system calculates the **personalized satisfaction score** for each product by adding the **base satisfaction** and the **relevance points** calculated in Step 4.
2. This personalized satisfaction score reflects how appealing each product is to the specific recipient.

**Example Calculation**:
- **Wireless Earbuds**:
  - Base Satisfaction: `80`
  - Relevance Points: `20`
  - **Personalized Satisfaction** = `80 + 20 = 100`

---

### Step 6: Generate an Initial Gift Bundle with the Greedy Algorithm

**Process**:
1. The system uses the **Greedy Algorithm** to create an initial gift bundle based on **personalized satisfaction per dollar** (personalized satisfaction divided by price).
2. Products are sorted by their value per dollar and added to the bundle until the budget is reached.

**Example Bundle**:
- Assume the bundle includes **Wireless Earbuds** ($50) and a **Phone Charger** ($20) for an initial cost of $70.

---

### Step 7: Refine the Bundle with the Genetic Algorithm

**Process**:
1. The system refines the initial bundle with the **Genetic Algorithm**.
2. It creates a **population** of bundles by introducing slight variations (e.g., swapping out products or adding new ones within the budget).
3. Each bundle’s **fitness** is evaluated based on the total personalized satisfaction and synergy points.
4. Through **selection, crossover, and mutation**, the Genetic Algorithm evolves to identify bundles with higher satisfaction.

**Example Result**:
- After several generations, a refined bundle is generated with a higher satisfaction score, potentially including a mix of tech and music-related items.

---

### Step 8: Final Optimization with Simulated Annealing

**Process**:
1. The **Simulated Annealing** algorithm makes final adjustments to the bundle by testing minor changes and accepting those that improve satisfaction.
2. The algorithm’s **temperature** parameter decreases over time, meaning it becomes less likely to accept lower-quality bundles as it progresses.
3. This process helps fine-tune the bundle to maximize the satisfaction score while avoiding local optima.

**Example Result**:
- The final bundle might replace one item with another that better fits the budget or provides higher synergy with the other products.

---

### Step 9: Calculate Synergy Points for the Final Bundle

**Process**:
1. The system calculates **synergy points** for the final bundle by evaluating pairs of products and checking for complementary (synergy) items.
2. `calculate_synergy` checks if pairs in the bundle complement each other (e.g., earbuds and a phone charger) and adds synergy points to the overall satisfaction score.

**Example**:
- The **Wireless Earbuds** and **Phone Charger** pair adds 15 synergy points to the final satisfaction score.

---

### Step 10: Display the Final Gift Bundle

**Process**:
1. The system presents the final bundle to the user, displaying:
   - **Selected Products**: Names and descriptions of the products in the bundle.
   - **Total Satisfaction Score**: Combined score from personalized satisfaction and synergy points.
   - **Total Cost**: Total price of the bundle, ensuring it stays within budget.

**Example Output**:
```plaintext
Final Gift Bundle:
1. Wireless Earbuds - $50
2. Phone Charger - $20
3. Bluetooth Speaker - $30

Total Satisfaction Score: 220
Total Cost: $100
```

This final bundle maximizes satisfaction within the budget, considering the recipient’s interests, product synergy, and personalization.
