from Products.CMFCore.utils import getToolByName

PROFILE = "profile-collective.js.datatables:default"


def common(context):
    """Just apply the prefix"""
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)
