#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the ios facts module.
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class FactsArgs(object):
    """ The arg spec for the ios facts module
    """

    def __init__(self, **kwargs):
        pass

    choices = [
        'all',
        '!all',
        'interfaces',
        '!interfaces',
        'l2_interfaces',
        '!l2_interfaces',
        'vlans',
        '!vlans',
    ]

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list'),
        'gather_network_resources': dict(choices=choices, type='list'),
    }
