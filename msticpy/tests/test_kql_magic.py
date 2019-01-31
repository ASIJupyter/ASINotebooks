# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""security_alert test class."""
import sys
import unittest
import pandas as pd

from IPython import get_ipython, embed_kernel

from .. asitools import kql
from .. asitools.security_alert_graph import create_alert_graph
from .. asitools.nbdisplay import display_alert

class TestKqlMagic(unittest.TestCase):

    _WS = '802d39e1-9d70-404d-832c-2de5e2478eda'
    query = '''
SecurityAlert
| take 1
    '''

    def setUp(self):
        pass
                
    def test_kql_magic(self):
        """Run query using KqlMagic"""
        self.assertTrue(True)