"""
"""

from wheezy.validation import Validator
from wheezy.validation.rules import length
from wheezy.validation.rules import required

from membership.rules import password_rules


credential_validator = Validator({
    'username': [required, length(min=2), length(max=20)],
    'password': password_rules
})
