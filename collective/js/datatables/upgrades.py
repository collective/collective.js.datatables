from Products.CMFCore.utils import getToolByName

PROFILE = "profile-collective.js.datatables:default"


def common(context):
    """Just apply the prefix"""
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)

def to2001(context):
    """Just apply the prefix"""
    setup = getToolByName(context, 'portal_setup')
    css = getToolByName(context, 'portal_css')
    js = getToolByName(context, 'portal_javascripts')
    setup.runImportStepFromProfile(PROFILE, 'jsregistry')
    setup.runImportStepFromProfile(PROFILE, 'cssregistry')
    css.cookResources()
    js.cookResources()
