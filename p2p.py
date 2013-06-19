#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'is_p2p_domain',
    'is_p2p_t3ld',
    'is_p2p_t2ld',
    'is_p2p_sld',
]
print('Executing %s' %  __file__)

from os.path import join, dirname
import cPickle as pickle

PATH = join(dirname(__file__), '@data', 'p2p')

p2p_kwset = set(w.strip() for w in
    open(join(PATH, 'p2p_keywords.@r.txt')) if not w.startswith('#'))


def is_p2p_domain (domain):
    """ Returns True if the given domain is related to P2P.
    """
    global p2p_kwset
    for kw in p2p_kwset:
        if kw in domain:
            return True
    return False

def is_p2p_t2ld (t2ld):
    pass

def is_p2p_sld (sld):
    pass

def is_p2p_t3ld (t3ld):
    pass

