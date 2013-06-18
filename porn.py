#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'Porn',
    'is_porn_domain',
]

from os.path import join, dirname

import meta

class Porn (object):
    """
    """
    __metaclass__ = meta.Singleton
    path = join(dirname(__file__), '@data', 'porn')

    def __init__ (self):
        """
        """
        print 'Calling Porn.__init__()'
        with open(join(self.path, 'porn_keywords.@r.txt'), 'r') as fr:
            self.porn_kwset = set(w.strip() for w in fr if not w.startswith('#'))


###############################################################################

porn = Porn()

def is_porn_domain (domain):
    """ Returns True if the given domain (i.e. FQDN) is a porn site.
        Note: incomplete. See cedns.dns_tools.is_porn
    """
    assert isinstance(domain, str)
    for kw in porn.porn_kwset:
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


if __name__ == '__main__':
    print porn.porn_kwset
    print 'Done.'
