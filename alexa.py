#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""

"""
__all__ = [
    'get_alexa_rank',
]
print('Executing %s' %  __file__)

from os.path import join, dirname
import cPickle as pickle


t2ld_to_alexarank = {}
PATH = join(dirname(__file__), '@data', 'alexa')

if __name__ == '__main__':
    with open(join(PATH, 'alexa-top-1m.@r.csv'), 'r') as fr:
        for line in fr:
            fields = line.strip().split(',')
            rank = int(fields[0])
            t2ld = fields[1]
            t2ld_to_alexarank [t2ld] = rank
    with open(join(PATH, 't2ld_to_alexarank.pk'), 'wb') as fw:
        pickle.dump(t2ld_to_alexarank, fw, protocol=2)
else:
    with open(join(PATH, 't2ld_to_alexarank.pk'), 'rb') as fr:
        t2ld_to_alexarank = pickle.load(fr)


def get_alexa_rank (t2ld):
    return t2ld_to_alexarank.get(t2ld, None)

