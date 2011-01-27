from zope.interface import Interface


class ICollectiveCarouselLayer(Interface):
    """ A layer specific to collective.carousel
    """


class ICarouselProvider(Interface):
    """ We should be able to mark objects that can be used in carousel with
        the special marker. For now this marks Collections only.
    """

ILeadImageable = None

try:
    from collective.contentleadimage.interfaces import ILeadImageable
except:
    pass

from Products.ATContentTypes.interface import IATContentType
from Products.ATContentTypes.interface import IATNewsItem

if ILeadImageable is not None:
    # Need to make sure we come up top
    class IATWithLeadImage(ILeadImageable, IATContentType):
        """ More specific interface """

    class IATNewsItemWithLeadImage(ILeadImageable, IATNewsItem):
        """ More specific interface """
