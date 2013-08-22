from Products.CMFCore.utils import getToolByName


def run_all_import_steps(context):
    context = getToolByName(context, "portal_setup")
    context.runAllImportStepsFromProfile(
        'profile-collective.carousel:default',
        purge_old=False)
