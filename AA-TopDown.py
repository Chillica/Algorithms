# -*- coding: utf-8 -*-
"""
Jacob Ashcraft
Top Down Algorithm
Advanced Algorithms
Professor Teichert

"""

from collections import namedtuple

def knapval_rep(capacity, items):
    """
    Returns the maximum value achievable in 'capacity'
    weight using 'items' when repeated items are allowed
    """
    options = list(
        item.value + knapval_rep(capacity-item.weight, items) for item in items if item.weight <= capacity)
    if len(options):
        return max(options)
    else:
        return 0

# def knapval_norep(capacity, items):
#     """
#     Returns the maximum value achievable in 'capacity'
#     weight using 'items' when repeated items are allowed
#     """
#     options = list(
#         item.value + knapval_norep(capacity-item.weight, items, list(for i in items if i is not item))  for item in items if item.weight <= capacity)
#     if len(options):
#         return max(options)
#     else:
#         return 0

Item = namedtuple('Item', ['weight', 'value'])

def test_kanpval_rep():
    loot = [
        Item(6,30),
        Item(3,14),
        Item(4,16),
        Item(2,9),
    ]

    assert knapval_rep(10, loot) == 48