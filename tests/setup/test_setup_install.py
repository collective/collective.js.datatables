from collective.js.datatables import PACKAGE_NAME
from plone import api


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if collective.js.datatables is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "2001"

    def test_jsregistry(self, portal):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled")
        assert datatable is True
        assert "++resource++jquery.datatables.min.js" in api.portal.get().view()

    def test_cssregistry(self, portal):
        datatable = api.portal.get_registry_record("plone.bundles/datatables.enabled")
        assert datatable is True
        assert "++resource++jquery.datatables/media/css/jquery.dataTables.css" in api.portal.get().view()