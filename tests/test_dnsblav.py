#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CONTRIBUTORS (sorted by surname)
# LUO, Pengkui <pengkui.luo@gmail.com>
#
# UPDATED ON
# 2013: 06/12,
#
"""
Unit tests

"""
import unittest

import domainutils as dmu


class Test_DNSBLAV (unittest.TestCase):

    def test_is_dnsav (self):
        self.assertTrue(dmu.is_dnsav('abcdefg.avqs.mcafee.com'))

    def test_is_dnsblav (self):
        self.assertTrue(dmu.is_dnsblav('abcdefg.avqs.mcafee.com'))
        self.assertTrue(dmu.is_dnsblav('xxxxxxxxx.dnsbl.ahbl.org'))
        self.assertTrue(dmu.is_dnsblav('spam-trap.net'))
        self.assertFalse(dmu.is_dnsblav('mail.google.com'))


if __name__ == '__main__':
    unittest.main()
