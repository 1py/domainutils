#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'Alexa',
    'get_alexa_rank',
]
from os.path import join, dirname
import cPickle as pickle

import pandas as pd
import meta


class Alexa (object):
    """
    """
    __metaclass__ = meta.Singleton
    path = join(dirname(__file__), '@data', 'alexa')

    def __init__ (self, rebuild=False):
        """
        """
        print 'Calling Alexa.__init__()'
        if rebuild:
            self.t2ld_to_alexarank = {}
            with open(join(self.path, 'alexa-top-1m.@r.csv'), 'r') as fr:
                for line in fr:
                    fields = line.strip().split(',')
                    rank = int(fields[0])
                    t2ld = fields[1]
                    self.t2ld_to_alexarank [t2ld] = rank
            with open(join(self.path, 't2ld_to_alexarank.pk'), 'wb') as fw:
                pickle.dump(self.t2ld_to_alexarank, fw, protocol=2)
        else:
            with open(join(self.path, 't2ld_to_alexarank.pk'), 'rb') as fr:
                self.t2ld_to_alexarank = pickle.load(fr)


if __name__ == '__main__':
    alexa = Alexa(rebuild=True)
else:
    alexa = Alexa()


def get_alexa_rank (t2ld):
    return alexa.t2ld_to_alexarank.get(t2ld, -1)
