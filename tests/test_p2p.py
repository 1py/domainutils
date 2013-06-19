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


class Test_P2P (unittest.TestCase):

    def test_is_p2p_domain (self):
        self.assertFalse(dmu.is_p2p_domain('mail.google.com'))
        self.assertTrue(dmu.is_p2p_domain('bt.332.org'))


if __name__ == '__main__':
    unittest.main()
