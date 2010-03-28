from zope.component import queryMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from plone.portlet.collection import collection as base

PLMF = MessageFactory('collective.carousel')


class ICarouselPortlet(base.ICollectionPortlet):
    """A portlet displaying a carousel with a Collection's results
    """

class Assignment(base.Assignment):
    implements(ICarouselPortlet)
    
    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave.
        """
        return self.header or u"Carousel portlet"
        
class Renderer(base.Renderer):
    render = ViewPageTemplateFile('carousel.pt')
    
    def use_view_action(self):
        portal_properties = getToolByName(self.context, 'portal_properties', None)
        site_properties = getattr(portal_properties, 'site_properties', None)
        use_view_action = site_properties.getProperty('typesUseViewActionInListings', ())
        return use_view_action        

    def get_tile(self, obj):
        # When adapter is uesd this means we check whether obj has any special 
        # instructions about how to be handled in defined view or interface
        # for multi adapter the same is true except more object than just the 
        # obj are check for instructions
        tile = queryMultiAdapter((obj, self.request), name="carousel-portlet-view")
        if tile is None:
            return None
        return tile()

class AddForm(base.AddForm):
    label = u"Add Carousel Portlet"
    description = u"This portlet display a listing of items from a Collection as a carousel."
    
    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    label = u"Edit Carousel Portlet"
    description = u"This portlet display a listing of items from a Collection as a carousel."
