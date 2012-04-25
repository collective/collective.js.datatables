import unittest2 as unittest
from collective.js.datatables.tests import base
from plone.browserlayer import utils

class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_jsregistry(self):
        pass

    def test_cssregistry(self):
        pass

class TestUninstall(base.IntegrationTestCase):
    """Test if the addon uninstall well"""

    def setUp(self):
        super(TestUninstall, self).setUp()
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=['collective.js.datatables'])

    def test_jsregistry(self):
        pass

    def test_cssregistry(self):
        pass

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)