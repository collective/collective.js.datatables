import transaction
import unittest2 as unittest
from zope import interface
from plone.app import testing
from collective.js.datatables import testing as layer

class UnitTestCase(unittest.TestCase):

    def setUp(self):
        pass

class IntegrationTestCase(unittest.TestCase):

    layer = layer.INTEGRATION

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

class FunctionalTestCase(IntegrationTestCase):

    layer = layer.FUNCTIONAL

    def setUp(self):
        #we must commit the transaction
        transaction.commit()
