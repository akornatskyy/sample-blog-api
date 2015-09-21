"""
"""

from wheezy.validation import Validator
from wheezy.validation.rules import length
from wheezy.validation.rules import required


search_posts_validator = Validator({
    'q': [length(max=20)],
    'page': []
})

post_comment_validator = Validator({
    'message': [required, length(min=2), length(max=250)]
})
