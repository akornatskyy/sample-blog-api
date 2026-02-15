from wheezy.validation import Validator
from wheezy.validation.rules import iterator
from wheezy.validation.rules import length
from wheezy.validation.rules import one_of
from wheezy.validation.rules import range
from wheezy.validation.rules import required


slug_rules = [required, length(min=2), length(max=35)]

search_posts_validator = Validator({
    'q': [length(max=20)],
    'page': [range(min=0), range(max=9)]
})

post_spec_validator = Validator({
    'slug': slug_rules,
    'fields': [iterator([one_of(('', 'permissions', 'comments'))])]
})

post_comment_validator = Validator({
    'slug': slug_rules,
    'message': [required, length(min=2), length(max=250)]
})
