from Products.CMFCore.utils import getToolByName

def upgrade(context):
    context.runImportStepFromProfile('profile-collective.js.datatables:default', 'jsregistry')