#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CONTRIBUTORS (sorted by surname)
# LUO, Pengkui <pengkui.luo@gmail.com>
#
# UPDATED ON
# 2013: 06/10, 06/12
#
print('Executing %s' %  __file__)

import unittest

import domainutils as dmu


class Test_TKLD (unittest.TestCase):

    def test_tklds (self):
        domain = 'a.mail.google.com'
        t2ld = dmu.get_t2ld (domain)
        t3ld = dmu.get_t3ld (domain, t2ld=t2ld)
        sld, tld = dmu.get_sld_tld (domain, t2ld=t2ld)
        self.assertEqual(tld, 'com')
        self.assertEqual(t2ld, 'google.com')
        self.assertEqual(t3ld, 'mail.google.com')


if __name__ == '__main__':
    unittest.main()
