#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'is_dnsav',
    'is_dnsbl',
    'is_dnsblav',
]
print('Executing %s' %  __file__)

from os.path import join, dirname
import cPickle as pickle

from .tkld import get_t2ld, get_t3ld


PATH = join(dirname(__file__), '@data', 'dnsblav')

dnsav_suffixset = set(w.strip() for w in
    open(join(PATH, 'dnsav_suffixes.@r.txt')) if not w.startswith('#'))

dnsbl_suffixset = set(w.strip() for w in
    open(join(PATH, 'dnsbl_suffixes.@r.txt')) if not w.startswith('#'))


def is_dnsav (domain):
    for suffix in dnsav_suffixset:
        if domain.endswith(suffix):
            return True
    return False

def is_dnsbl (t2ld, t3ld):
    if t2ld in dnsbl_suffixset or t3ld in dnsbl_suffixset:
        return True
    else: return False

def is_dnsblav (domain):
    t2ld = get_t2ld (domain)
    t3ld = get_t3ld (domain, t2ld=t2ld)
    if is_dnsav(domain) or is_dnsbl(t2ld, t3ld):
        return True
    else: return False
