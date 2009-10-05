from zope.interface import Interface
from plone.app.portlets.interfaces import IColumn

class ICollectiveCarouselLayer(Interface):
    """A layer specific to collective.carousel
    """

class ICarouselPortletsRow(IColumn):
    """ Carousel Portlets Row is a portlet manager that sits atop of content
        and is supposed to contain collection portlet represented as a carousel
    """
