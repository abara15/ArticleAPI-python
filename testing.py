from math import exp
import unittest

from app import get_article, get_tag_summary

class Tests(unittest.TestCase):
    # Testing non-existent article
    def test_get_article(self):
        expected_result = "Please query for a valid article."
        result = get_article(1000);
        self.assertEqual(expected_result, result)
    
    # Testing Article #1
    def test_get_article_valid(self):
        expected_result = {
            "body": "some text, potentially containing simple markup about how potato chips are great",
            "date": "2022-04-20",
            "id": 1,
            "tags": [
                "health",
                "fitness",
                "science"
            ],
            "title": "latest science shows that potato chips are better for you than sugar"
        }
        result = get_article(1)
        self.assertEqual(expected_result, result)
    
    # Testing non-existent tag
    def test_tag_summary_bad_tag(self):
        expected_result = "No articles associated with the given tag and date."
        result = get_tag_summary("lol", "20220420")
        self.assertEqual(expected_result, result)
    
    # Testing non-existent date
    def test_tag_summary_bad_date(self):
        expected_result = "No articles associated with the given tag and date."
        result = get_tag_summary("health", "20100420")
        self.assertEqual(expected_result, result)
    
    # Testing tag summary for health
    def test_get_tag_summary(self):
        expected_result = {
            "articles": [
                1,
                2
            ],
            "count": 2,
            "related_tags": [
                "fitness",
                "science",
                "covid",
                "australia"
            ],
            "tag": "health"
        }
        result = get_tag_summary("health", "20220420")
        self.assertEqual(expected_result, result)
    
if __name__ == '__main__':
    unittest.main()