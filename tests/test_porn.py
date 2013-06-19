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


class Test_Porn (unittest.TestCase):

    def test_is_porn_domain (self):
        self.assertFalse(dmu.is_porn_domain('mail.google.com'))
        self.assertTrue(dmu.is_porn_domain('boobs.com'))
        self.assertTrue(dmu.is_porn_domain('adultvideo.com'))


if __name__ == '__main__':
    unittest.main()
