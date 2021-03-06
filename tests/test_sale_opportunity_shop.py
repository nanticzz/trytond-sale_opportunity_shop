# This file is part of the sale_opportunity_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleOpportunityShopTestCase(ModuleTestCase):
    'Test Sale Opportunity Shop module'
    module = 'sale_opportunity_shop'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleOpportunityShopTestCase))
    return suite
