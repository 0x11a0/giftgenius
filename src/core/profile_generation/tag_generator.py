import openai
import os
from config import config  # Import configuration settings

# Initialize OpenAI with the API key
openai.api_key = config.OPENAI_API_KEY

def generate_tags(description):
    """
    Uses OpenAI API to generate interest tags based on the recipient's description.
    :param description: A text description about the recipient.
    :return: A list of generated tags based on interests inferred from the description.
    """
    prompt = f"Generate concise interest tags based on the following description: '{description}'. Each tag should capture a main interest or personality trait. Return a comma-separated list of relevant tags."

    try:
        response = openai.ChatCompletion.create(
            model=config.OPENAI_MODEL,  # Use gpt-3.5-turbo or other supported model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides interest tags."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.7,
        )

        # Extract the generated tags from the response
        tags_text = response['choices'][0]['message']['content'].strip()
        if not tags_text:
            return []  # Return an empty list if no tags are generated

        tags = [tag.strip() for tag in tags_text.split(",")]
        return tags

    except Exception as e:  # Catch any API-related errors
        print(f"Error generating tags: {e}")
        return []
