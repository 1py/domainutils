#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'is_porn_domain',
]
print('Executing %s' %  __file__)

from os.path import join, dirname


PATH = join(dirname(__file__), '@data', 'porn')

with open(join(PATH, 'porn_keywords.@r.txt'), 'r') as fr:
    porn_kwset = set(w.strip() for w in fr if not w.startswith('#'))


def is_porn_domain (domain):
    """ Returns True if the given domain (i.e. FQDN) is a porn site.
        Note: incomplete. See cedns.dns_tools.is_porn
    """
    global porn_kwset
    for kw in porn_kwset:
        if kw in domain:
            return True
    # check via WOT
    return False

def is_porn_t2ld (t2ld):
    pass

def is_porn_sld (sld):
    pass

def is_porn_t3ld (t3ld):
    pass
