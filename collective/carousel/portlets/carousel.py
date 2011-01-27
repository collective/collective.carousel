from zope.i18nmessageid import MessageFactory
from zope.interface import implements
from zope import schema
from zope.formlib import form
from AccessControl import SecurityManagement

from Products.ATContentTypes.permission import ChangeTopics
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

    timer = schema.Float(
        title=_(u"Timer"),
        description=_(u"Length of time before automatically move to next \
                        tile (seconds)"),
        required=False,
        default=25.0)


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
    timer = 25.0

    def __init__(self, header=u"", target_collection=None, limit=None,
                 random=False, show_more=True, show_dates=False,
                 omit_border=True, hide_controls=False, timer=25.0):
        super(Assignment, self).__init__(header=header,
                                         target_collection=target_collection,
                                         limit=limit,
                                         random=random,
                                         show_more=show_more,
                                         show_dates=show_dates)
        self.omit_border = omit_border
        self.hide_controls = hide_controls
        self.timer = timer

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave.
        """
        return self.header or u"Carousel portlet"


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('carousel.pt')

    def use_view_action(self):
        pp = getToolByName(self.context, 'portal_properties', None)
        sp = getattr(pp, 'site_properties', None)
        use_view_action = sp.getProperty('typesUseViewActionInListings', ())
        return use_view_action

    def get_tile(self, obj):
        # When adapter is uesd this means we check whether obj has any special
        # instructions about how to be handled in defined view or interface
        # for multi adapter the same is true except more object than just the
        # obj are check for instructions

        #have to use traverse to make zpt security work
        tile = obj.unrestrictedTraverse("carousel-portlet-view")
        if tile is None:
            return None
        return tile()

    def canSeeEditLink(self):
        provider = self.collection()
        smanager = SecurityManagement.getSecurityManager()
        return smanager.checkPermission(ChangeTopics, provider)

    def editCarouselLink(self):
        provider = self.collection()
        if provider is not None:
            return provider.absolute_url() + '/criterion_edit_form'
        return None

    def getTimer(self):
        """ return timer in ms"""
        if getattr(self.data, 'timer', None) is not None:
            return int(self.data.timer*1000)
        else:
            return 25000


class AddForm(base.AddForm):
    form_fields = form.Fields(ICarouselPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget

    label = _(u"Add Carousel Portlet")
    description = _(u"This portlet display a listing of items from a \
                      Collection as a carousel.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(ICarouselPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget

    label = _(u"Edit Carousel Portlet")
    description = _(u"This portlet display a listing of items from a \
                      Collection as a carousel.")
