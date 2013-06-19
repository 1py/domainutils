# -*- coding: utf-8 -*-
#
# (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 6/12/2013, updated 6/18/2013
#
""" Utilities for domain names.

    Suggested Usage:
    >>> import domainutils as dmu
    >>> t2ld = dmu.get_t2ld('a.mail.google.com')
    >>> ...

"""
from __future__ import absolute_import

__all__ = [
    # tkld.py
    'get_t2ld',
    'get_sld_tld',
    'get_t3ld',
    'is_fqdn',
    # dnsblav.py
    'is_dnsav',
    'is_dnsbl',
    'is_dnsblav',
    # alexa.py
    'get_alexa_rank',
    # p2p.py
    'is_p2p_domain',
    # porn.py
    'is_porn_domain',
    # hostname.py
    'is_valid_hostname',
]
print('Executing %s' %  __file__)

import sys
if sys.version_info[:2] < (2, 6):
    raise ImportError("CPython 2.6.x or above is required (%d.%d detected)."
                      % sys.version_info[:2])

from .tkld import *
from .dnsblav import *
from .alexa import *
from .p2p import *
from .porn import *
from .hostname import *

del sys, absolute_import

__version__ = '0.1.2'
