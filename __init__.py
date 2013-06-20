# -*- coding: utf-8 -*-
#
# (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 6/12/2013, updated 6/19/2013
#
""" Utilities for domain names.

"""
from __future__ import absolute_import

__all__ = [
    # hostname.py
    'is_valid_hostname',
]
print('Executing %s' %  __file__)

import sys
if sys.version_info[:2] < (2, 6):
    raise ImportError("CPython 2.6.x or above is required (%d.%d detected)."
                      % sys.version_info[:2])

from .hostname import *

del sys, absolute_import

__version__ = '0.1.3'
