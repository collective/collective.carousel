from zope.component import adapts
from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATContentTypes.interface import IATContentType
from Products.Archetypes.public import ReferenceField

from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField

from collective.carousel.interfaces import ICollectiveCarouselLayer

_ = MessageFactory('collective.carousel')

class CarouselProviderField(ExtensionField, ReferenceField):
   """A field, storing reference to an object, providing 
      content for carousel
   """

class ContentTypeExtender(object):
    adapts(IATContentType)
    implements(ISchemaExtender,
               IBrowserLayerAwareExtender)
    layer = ICollectiveCarouselLayer

    _fields = [
        CarouselProviderField("carouselprovider",
            schemata = "settings",
            # the field accepts Collections only atm. 
            # Would be cool to have ATRBW to be able to select items by interface
            # with something like 'allowed_interfaces'
            allowed_types = ('Topic'),
            relationship = 'Carousel',
            languageIndependent = True,
            multiValued = True,
            widget = ReferenceBrowserWidget(
                label = _(u"label_carouselprovider_title",
                    default=u"Carousel object."),
                description = _(u"help_carouselprovider",
                    default=u"Object providing items (content) for carousel."),
                ),
            ),
        ]
        
    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self._fields