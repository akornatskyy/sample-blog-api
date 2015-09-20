"""
"""

from wheezy.validation import Validator
from wheezy.validation.rules import length


search_posts_validator = Validator({
    'q': [length(max=20)],
    'page': []
})
