from Products.CMFCore.utils import getToolByName

def upgrade_1901(context):
    """Since the resource name stays the same, we just need to re-generate our
    Javascripts.
    """
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.cookResources()
