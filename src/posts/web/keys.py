def post_public(post_slug):
    return 'pstp:' + post_slug + ':'


def post(post_slug):
    return 'post:' + post_slug + ':'


def author_comments(author_id):
    return 'poco:' + author_id + ':'
