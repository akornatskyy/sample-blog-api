def search_posts(q, page):
    return 'p:sepo:' + q + ':' + str(page)


def get_post_id(slug):
    return 'p:gpid:' + slug


def get_post(slug):
    return 'p:gepo:' + slug


def list_comments(post_id, author_id):
    if author_id:
        return 'p:lico:' + str(post_id) + ':' + author_id
    return 'p:lice:' + str(post_id)


def count_comments_awaiting_moderation(user_id, limit=None):
    return 'p:ccam:' + user_id
