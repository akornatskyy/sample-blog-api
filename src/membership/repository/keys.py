"""
"""


def authenticate(username):
    return 'm:auth:' + username


def get_user(user_id):
    return 'm:geus:' + str(user_id)


def has_account(username):
    return 'm:haac:' + username
