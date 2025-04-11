import unittest
from collective.js.datatables.tests import base
from plone.browserlayer import utils
from plone import api
from Products.CMFPlone.utils import get_installer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_jsregistry(self):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled")
        self.assertTrue(datatable is True)
        self.assertTrue("++resource++jquery.datatables.min.js" in api.portal.get().view())


    def test_cssregistry(self):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled")
        self.assertTrue(datatable is True)
        self.assertTrue("++resource++jquery.datatables/media/css/jquery.dataTables.css" in api.portal.get().view())

class TestUninstall(base.IntegrationTestCase):
    """Test if the addon uninstall well"""

    def setUp(self):
        super(TestUninstall, self).setUp()
        self.portal = self.layer["portal"]
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product("collective.js.datatables")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_jsregistry(self):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled")
        __import__("pdb").set_trace()
        self.assertTrue(datatable is False)
        self.assertTrue("++resource++jquery.datatables.min.js" not in api.portal.get().view())

    def test_cssregistry(self):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled")
        self.assertTrue(datatable is False)
        self.assertTrue("++resource++jquery.datatables/media/css/jquery.dataTables.css" not in api.portal.get().view())

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)