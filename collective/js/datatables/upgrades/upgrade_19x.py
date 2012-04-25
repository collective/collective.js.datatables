from Products.CMFCore.utils import getToolByName

def upgrade_1901(context):
    """Since the resource name stays the same, we just need to re-generate our
    Javascripts.
    """
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.cookResources()

def upgrade_1902(context):
    """register css if not already done"""
    cssregistry = getToolByName(context, 'portal_css')
    cssid = '++resource++jquery.datatables/media/css/jquery.dataTables.css'
    css = cssregistry.getResource(cssid)
    if css is None:
        setup = getToolByName(context, 'portal_setup')
        setup.runImportStepFromProfile('profile-collective.js.datatables:default',
                                       'cssregistry', run_dependencies=False,
                                       purge_old=False)
