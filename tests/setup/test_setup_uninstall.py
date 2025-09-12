from collective.js.datatables import PACKAGE_NAME
from plone import api

import pytest


class TestSetupUninstall:
    @pytest.fixture(autouse=True)
    def uninstalled(self, installer):
        installer.uninstall_product(PACKAGE_NAME)

    def test_addon_uninstalled(self, installer):
        """Test if collective.js.datatables is uninstalled."""
        assert installer.is_product_installed(PACKAGE_NAME) is False

    def test_jsregistry(self, portal):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled", default=False)
        assert datatable is False
        assert "++resource++jquery.datatables.min.js" not in api.portal.get().view()

    def test_cssregistry(self, portal):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled", default=False)
        assert datatable is False
        assert "++resource++jquery.datatables/media/css/jquery.dataTables.min.css" not in api.portal.get().view()
