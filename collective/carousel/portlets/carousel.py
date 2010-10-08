from zope.component import queryMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.interface import implements
from zope import schema
from zope.formlib import form

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from plone.portlet.collection import collection as base
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

_ = MessageFactory('collective.carousel')


class ICarouselPortlet(base.ICollectionPortlet):
    """A portlet displaying a carousel with a Collection's results
    """
    omit_border = schema.Bool(
        title=_(u"Omit portlet border"),
        description=_(u"Tick this box if you want to render the text above "
                      "without the standard header, border or footer."),
        required=True,
        default=True)

    hide_controls = schema.Bool(
        title=_(u"Hide controls"),
        description=_(u"Tick this box if you want to temporarily hide "
                      "carousel controls i.e. next, prev, pause buttons."),
        required=True,
        default=False)

class Assignment(base.Assignment):
    implements(ICarouselPortlet)
    
    header = u""
    target_collection=None
    limit = None
    random = False
    show_more = True
    show_dates = False
    omit_border = True
    hide_controls = False

    def __init__(self, header=u"", target_collection=None, limit=None,
                 random=False, show_more=True, show_dates=False,
                 omit_border=True, hide_controls=False):
        super(Assignment, self).__init__(header=header,
                                         target_collection=target_collection, 
                                         limit=limit,
                                         random=random,
                                         show_more=show_more,
                                         show_dates=show_dates)
        self.omit_border = omit_border
        self.hide_controls = hide_controls

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
    form_fields = form.Fields(ICarouselPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget

    label = _(u"Add Carousel Portlet")
    description = _(u"This portlet display a listing of items from a Collection as a carousel.")
    
    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(ICarouselPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget

    label = _(u"Edit Carousel Portlet")
    description = _(u"This portlet display a listing of items from a Collection as a carousel.")
