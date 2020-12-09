"""
"""

import json
import os.path

from wheezy.core.collections import attrdict


def trancate_words(s, count):
    s = list(filter(None, s.replace('\\n', ' ').split(' ', count + 1)[:-1]))
    if len(s) == count:
        s.append('...')
    return ' '.join(s)


def pager(items, page, size, f):
    start = page * size
    end = start + size
    n = len(items)
    paging = {}
    if page > 0:
        paging['before'] = page - 1

    if end < n:
        paging['after'] = page + 1
    else:
        end = n
    return {
        'paging': paging,
        'items': [f(i) for i in items[start:end]]
    }


def first(items, predicate):
    return next(filter(predicate, items), None)


def nfilter(items, n, predicate):
    r = []
    for i in items:
        if predicate(i):
            r.append(i)
            n -= 1
            if not n:
                break
    return r


def load_samples(module_file):
    return json.load(open(os.path.join(
        os.path.dirname(os.path.realpath(module_file)),
        'samples.json')), object_hook=attrdict)
