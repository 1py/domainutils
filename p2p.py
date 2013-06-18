#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'P2P',
    'is_p2p_domain',
    'is_p2p_t3ld',
    'is_p2p_t2ld',
    'is_p2p_sld',
]

from os.path import join, dirname
import cPickle as pickle

import meta

class P2P (object):
    """
    """
    __metaclass__ = meta.Singleton
    path = join(dirname(__file__), '@data', 'p2p')

    def __init__ (self):
        """
        """
        print 'Calling P2P.__init__()'
        self.p2p_kwset = set(w.strip() for w in
            open(join(self.path, 'p2p_keywords.@r.txt'))
            if not w.startswith('#')
        )


###############################################################################

p2p = P2P()

def is_p2p_domain (domain):
    """ Returns True if the given domain is related to P2P.
    """
    assert isinstance(domain, str)
    for kw in p2p.p2p_kwset:
        if kw in domain:
            return True
    return False

def is_p2p_t2ld (t2ld):
    pass

def is_p2p_sld (sld):
    pass

def is_p2p_t3ld (t3ld):
    pass

if __name__ == '__main__':
    print p2p.p2p_kwset
    print 'Done.'
