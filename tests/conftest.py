from collective.js.datatables.testing import ACCEPTANCE_TESTING
from collective.js.datatables.testing import FUNCTIONAL_TESTING
from collective.js.datatables.testing import INTEGRATION_TESTING
from pathlib import Path
from plone import api
from pytest_plone import fixtures_factory
from requests.exceptions import ConnectionError
from zope.component.hooks import setSite

import pytest
import requests


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (ACCEPTANCE_TESTING, "acceptance"),
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)