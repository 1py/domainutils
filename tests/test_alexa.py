#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CONTRIBUTORS (sorted by surname)
# LUO, Pengkui <pengkui.luo@gmail.com>
#
# UPDATED ON
# 2013: 06/12
#
print('Executing %s' %  __file__)

import unittest

import domainutils as dmu


class Test_Alexa (unittest.TestCase):

    def test_tklds (self):
        domain = 'a.mail.google.com'
        t2ld = dmu.get_t2ld (domain)
        self.assertLess(0, dmu.get_alexa_rank(t2ld))


if __name__ == '__main__':
    unittest.main()
