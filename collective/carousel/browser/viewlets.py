from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from AccessControl import SecurityManagement

from Products.ATContentTypes.permission import ChangeTopics
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.globals.interfaces import IViewView 


class CarouselViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/carousel.pt')

    def update(self):
        if IViewView.providedBy(self.__parent__):
            alsoProvides(self, IViewView)

    def getProviders(self):
        schema = getattr(self.context, 'Schema', None)
        if schema is None:
            return None
        field = schema().getField('carouselprovider')
        if field is None:
            return None
        return field.get(self.context)

    def results(self, provider):
        results = []
        if provider is not None:
            # by default we assume that only Collections are addable 
            # as a carousel provider
            
            # It doesn't make sense to show *all* objects from a collection 
            # - some of them might return hundreeds of objects
            return provider.queryCatalog()[:7]
        return results

    def canSeeEditLink(self, provider):
        smanager = SecurityManagement.getSecurityManager()
        return smanager.checkPermission(ChangeTopics, provider)

    def editCarouselLink(self, provider):
        if provider is not None:
            return provider.absolute_url() + '/criterion_edit_form'
        return None

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