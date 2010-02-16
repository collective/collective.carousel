from Acquisition import aq_inner
from zope.component import getUtility
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.interfaces import IPloneSiteRoot
from collective.contentleadimage.config import IMAGE_FIELD_NAME
from collective.contentleadimage.leadimageprefs import ILeadImagePrefsForm

class LeadImageTile(BrowserView):
    
#    template = ViewPageTemplateFile('templates/lead_image_tile.pt')
#    render = template

    @property
    def prefs(self):
        portal = getUtility(IPloneSiteRoot)
        return ILeadImagePrefsForm(portal)

    def tag(self, obj, css_class='tileImage'):
        """ return a tag for the leadimage"""
        context = aq_inner(obj)
        field = context.getField(IMAGE_FIELD_NAME)
        if field is not None:
            if field.get_size(context) != 0:
                #scale = self.prefs.body_scale_name
                scale = 'leadimage'
                return field.tag(context, scale=scale, css_class=css_class)
        return ''
    
    def __call__(self):
        return self.index()
