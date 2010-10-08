from Acquisition import aq_inner
from zope.component import getUtility
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.interfaces import IPloneSiteRoot
from collective.contentleadimage.config import IMAGE_FIELD_NAME
from collective.contentleadimage.leadimageprefs import ILeadImagePrefsForm

class LeadImageTile(BrowserView):
    
    template = ViewPageTemplateFile('templates/lead_image_tile.pt')
    render = template

    @property
    def prefs(self):
        portal = getUtility(IPloneSiteRoot)
        return ILeadImagePrefsForm(portal)

    def tag(self, css_class='tileImage'):
        """ return a tag for the leadimage"""
        context = aq_inner(self.context)
        
        field = context.getField(IMAGE_FIELD_NAME)
        if field is not None:
            if field.get_size(context) != 0:
                #scale = self.prefs.body_scale_name
                scale = 'leadimage'
                return field.tag(context, scale=scale, css_class=css_class)

        if getattr(context,'tag', None) is not None:
            return context.tag(scale='preview', css_class=css_class)

        return ''


    def caption(self):
        context = aq_inner(self.context)
        field = context.getField(IMAGE_CAPTION_FIELD_NAME)
        if field is None:
            return ''

        return context.widget(IMAGE_CAPTION_FIELD_NAME, mode='view')
        
    def isAllowed(self):
        context = aq_inner(self.context)
        portal_type = getattr(context, 'portal_type', None)
        if portal_type in self.prefs.allowed_types:
            return super(LeadImageViewlet, self).render()
        else:
            return ''

    
    def __call__(self):
        return self.render()
        
        
