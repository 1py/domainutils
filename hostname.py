#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CONTRIBUTORS (sorted by surname)
# LUO, Pengkui <pengkui.luo@gmail.com>
#
#
# UPDATED ON
# 2013: 06/12,
#
"""
Utility functions

"""
__all__ = [
    'is_valid_hostname',
]

import re


HOSTNAME_ALLOWED_CHARS = re.compile("(?!-)[a-zA-Z\d-]{1,63}(?<!-)$")


def is_valid_hostname (hostname):
    """
    Determines if a hostname is syntactically valid (without DNS resolution).

    http://stackoverflow.com/questions/2532053/validate-hostname-string-in-python
    'Any domain name is syntactically valid if it's a dot-separated list of
    identifiers, each no longer than 63 characters, and made up of letters,
    digits and dashes (no underscores?).'

    """
    if len(hostname) > 255:
        return False
    if hostname[-1:] == '.':  # strip the trailing dot
        hostname = hostname[:-1]
    return all(HOSTNAME_ALLOWED_CHARS.match(s) for s in hostname.split('.'))

