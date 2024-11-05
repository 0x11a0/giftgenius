import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch
from core.profile_generation.tag_generator import generate_tags

class TestTagGenerator(unittest.TestCase):
    
    @patch("core.profile_generation.tag_generator.openai.Completion.create")
    def test_generate_tags_successful(self, mock_openai):
        # Mock response from OpenAI API
        mock_openai.return_value.choices = [type("Choice", (object,), {"text": "Tech Lover, Music Enthusiast, Outdoorsy"})]
        
        description = "A tech-savvy music lover who enjoys outdoor activities."
        expected_tags = ["Tech Lover", "Music Enthusiast", "Outdoorsy"]
        
        # Call the function
        tags = generate_tags(description)
        
        # Assertions
        self.assertIsInstance(tags, list, "Expected tags to be a list.")
        self.assertEqual(tags, expected_tags, f"Expected tags {expected_tags}, but got {tags}.")

    @patch("core.profile_generation.tag_generator.openai.Completion.create")
    def test_generate_tags_empty_response(self, mock_openai):
        # Mock empty response from OpenAI API
        mock_openai.return_value.choices = [type("Choice", (object,), {"text": ""})]
        
        description = "A nature-loving photographer who travels frequently."
        tags = generate_tags(description)
        
        # Assertions
        self.assertIsInstance(tags, list, "Expected tags to be a list.")
        self.assertEqual(tags, [], "Expected empty list for no tags generated.")

    @patch("core.profile_generation.tag_generator.openai.Completion.create")
    def test_generate_tags_api_error(self, mock_openai):
        # Mock an API error
        mock_openai.side_effect = Exception("OpenAI API error")
        
        description = "An adventurous foodie and tech enthusiast."
        tags = generate_tags(description)
        
        # Assertions
        self.assertIsInstance(tags, list, "Expected tags to be a list.")
        self.assertEqual(tags, [], "Expected an empty list on API error.")

if __name__ == "__main__":
    unittest.main()