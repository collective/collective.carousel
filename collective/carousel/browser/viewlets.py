from zope.interface import alsoProvides

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.globals.interfaces import IViewView 

class CarouselViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/carousel.pt')

    def update(self):
        if IViewView.providedBy(self.__parent__):
            alsoProvides(self, IViewView)