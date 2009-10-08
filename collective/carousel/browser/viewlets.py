from zope.component import queryMultiAdapter
from zope.interface import alsoProvides

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.globals.interfaces import IViewView 

class CarouselViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/carousel.pt')

    def update(self):
        if IViewView.providedBy(self.__parent__):
            alsoProvides(self, IViewView)
          
    def getProviders(self):
        field = self.context.Schema().getField('carouselprovider')
        return field.get(self.context)
            
    def results(self, provider):
        results = []
        if provider is not None:
            # by default we assume that only Collections are addable 
            # as a carousel provider
            results = provider.queryCatalog()
        return results
            
    def use_view_action(self):
        portal_properties = getToolByName(self.context, 'portal_properties', None)
        site_properties = getattr(portal_properties, 'site_properties', None)
        use_view_action = site_properties.getProperty('typesUseViewActionInListings', ())
        return use_view_action        

    def get_tile(self, obj):
        # note to myself
        # When adapter is uesd this means we check whether obj has any special 
        # instructions about how to be handled in defined view or interface
        # for multi adapter the same is true except more object than just the 
        # obj are check for instructions
        tile = queryMultiAdapter((obj, self.request), name="carousel-view")
        if tile is None:
            return None
        return tile()