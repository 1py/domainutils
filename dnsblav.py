#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'DNSBLAV',
    'is_dnsav',
    'is_dnsbl',
    'is_dnsblav',
]

from os.path import join, dirname
import cPickle as pickle

import meta

from tkld import get_t2ld, get_t3ld


class DNSBLAV (object):
    """
    """
    __metaclass__ = meta.Singleton
    path = join(dirname(__file__), '@data', 'dnsblav')

    def __init__ (self):
        """
        """
        print 'Calling DNSBL.__init__()'
        self.dnsav_suffixset = set(w.strip() for w in
            open(join(self.path, 'dnsav_suffixes.@r.txt'))
            if not w.startswith('#'))

        self.dnsbl_suffixset = set(w.strip() for w in
            open(join(self.path, 'dnsbl_suffixes.@r.txt'))
            if not w.startswith('#'))


###############################################################################

dnsblav = DNSBLAV()

def is_dnsav (domain):
    for suffix in dnsblav.dnsav_suffixset:
        if domain.endswith(suffix):
            return True
    return False

def is_dnsbl (t2ld, t3ld):
    if t2ld in dnsblav.dnsbl_suffixset or t3ld in dnsblav.dnsbl_suffixset:
        return True
    else: return False

def is_dnsblav (domain):
    t2ld = get_t2ld (domain)
    t3ld = get_t3ld (domain, t2ld=t2ld)
    if is_dnsav(domain) or is_dnsbl(t2ld, t3ld):
        return True
    else: return False
