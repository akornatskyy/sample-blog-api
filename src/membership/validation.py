from wheezy.validation import Validator
from wheezy.validation.rules import compare
from wheezy.validation.rules import email
from wheezy.validation.rules import length
from wheezy.validation.rules import required

from membership.rules import password_rules


credential_validator = Validator({
    'username': [required, length(min=2), length(max=20)],
    'password': password_rules
})

password_match_validator = Validator({
    'password': [
        compare(
            equal='confirm_password',
            message_template='Passwords do not match.')
    ]
})

signup_validator = Validator({
    'email': [required, length(min=6), length(max=30), email],
    # 'first_name': [required, length(max=30)],
    # 'last_name': [required, length(max=30)]
})
