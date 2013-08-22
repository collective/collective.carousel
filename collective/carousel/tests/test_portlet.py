# Carousel is rendered through a viewlet in IAboveContent
# using items provided by the carousel provider added to the context
from collective.carousel.portlets import carousel
from collective.carousel.tests.base import TestCase
from plone.app.portlets.storage import PortletAssignmentMapping
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility, getMultiAdapter

# default test query
query = [{
    'i': 'portal_type',
    'o': 'plone.app.querystring.operation.selection.is',
    'v': ['Document', 'Event', 'News Item']
}]


class PortletTest(TestCase):

    def afterSetUp(self):
        """Set up the carousel Collection and some dummy objects"""

        self.setRoles('Manager')
        self.folder.invokeFactory('Collection', 'collection')
        collection = getattr(self.folder, 'collection')
        collection.setQuery(query)

        field = self.folder.Schema().getField('carouselprovider')
        field.set(self.folder, collection)

        # add a few objects
        self.folder.invokeFactory('Document', 'carousel-doc')
        self.folder.invokeFactory('News Item', 'carousel-news-item')
        self.folder.invokeFactory('Event', 'carousel-event')

    def testPortletTypeRegistered(self):
        portlet = getUtility(IPortletType, name='portlet.Carousel')
        self.assertEquals(portlet.addview, 'portlet.Carousel')

    def testInterfaces(self):
        portlet = carousel.Assignment(header=u"title")
        self.failUnless(IPortletAssignment.providedBy(portlet))
        self.failUnless(IPortletDataProvider.providedBy(portlet.data))

    def testInvokeAddview(self):
        portlet = getUtility(IPortletType, name='portlet.Carousel')
        mapping = self.portal.restrictedTraverse(
            '++contextportlets++plone.leftcolumn')
        for m in mapping.keys():
            del mapping[m]
        addview = mapping.restrictedTraverse('+/' + portlet.addview)
        addview.createAndAdd(data={'header': u"test title"})
        self.assertEquals(len(mapping), 1)
        self.failUnless(isinstance(mapping.values()[0], carousel.Assignment))

    def testInvokeEditView(self):
        mapping = PortletAssignmentMapping()
        request = self.folder.REQUEST
        mapping['foo'] = carousel.Assignment(header=u"title")
        editview = getMultiAdapter((mapping['foo'], request), name='edit')
        self.failUnless(isinstance(editview, carousel.EditForm))

    def testRenderer(self):
        context = self.folder
        request = self.folder.REQUEST
        view = self.folder.restrictedTraverse('@@plone')
        manager = getUtility(IPortletManager, name='plone.rightcolumn',
                             context=self.portal)
        assignment = carousel.Assignment(header=u"title")

        renderer = getMultiAdapter((context, request, view,
                                    manager, assignment),
                                   IPortletRenderer)
        self.failUnless(isinstance(renderer, carousel.Renderer))


class TestRenderer(TestCase):

    # default test query
    query = [{
        'i': 'portal_type',
        'o': 'plone.app.querystring.operation.selection.is',
        'v': ['Document', 'Event', 'News Item']
    }]

    def afterSetUp(self):
        self.setRoles(('Manager', ))
        self.folder.invokeFactory('Collection', 'collection')
        collection = getattr(self.folder, 'collection')
        collection.setQuery(query)

        field = self.folder.Schema().getField('carouselprovider')
        field.set(self.folder, collection)

        # add a few objects
        self.folder.invokeFactory('Document', 'carousel-doc')
        self.folder.invokeFactory('News Item', 'carousel-news-item')
        self.folder.invokeFactory('Event', 'carousel-event')

    def renderer(self, context=None, request=None, view=None,
                 manager=None, assignment=None):
        context = context or self.folder
        request = request or self.folder.REQUEST
        view = view or self.folder.restrictedTraverse('@@plone')
        manager = manager or getUtility(IPortletManager,
                                        name='plone.rightcolumn',
                                        context=self.portal)
        assignment = assignment or carousel.Assignment(header=u"title")

        return getMultiAdapter((context, request, view, manager, assignment),
                               IPortletRenderer)

    def test_render(self):
        r = self.renderer(context=self.portal,
                          assignment=carousel.Assignment(
                          header=u"title",
                          target_collection=
                          '/plone/Members/test_user_1_/collection'))
        r = r.__of__(self.folder)
        r.update()
        output = r.render()
        self.assertTrue('title' in output)

    def test_css_class(self):
        r = self.renderer(
            context=self.portal,
            assignment=carousel.Assignment(header=u"Test carousel"))
        self.assertEquals('portlet-carousel-test-carousel', r.css_class())

    def test_hideheader(self):
        r = self.renderer(
            context=self.portal,
            assignment=carousel.Assignment(header=u"Test carousel", hideheader=True))
        output = r.render()
        self.failUnless('class="portletHeader hiddenStructure"' in output)

    def test_portlet_collection(self):

        query = [{
            'i': 'portal_type',
            'o': 'plone.app.querystring.operation.selection.is',
            'v': ['Document']
        }]
        # add a few documents
        for i in range(6):
            self.folder.invokeFactory('Document', 'document_%s' % i)
            getattr(self.folder, 'document_%s' % i).reindexObject()

        collection = getattr(self.folder, 'collection')
        collection.setQuery(query)

        # the documents are returned by the collection
        collection_num_items = len(self.folder.collection.queryCatalog())
        # We better have some documents - we should have 8
        self.failUnless(collection_num_items >= 8)

        mapping = PortletAssignmentMapping()
        mapping['foo'] = carousel.Assignment(
            header=u"Test carousel",
            target_collection='/Members/test_user_1_/collection')
        r = self.renderer(context=None, request=None, view=None,
                          manager=None, assignment=mapping['foo'])

        # sanity check
        self.assertEqual(r.collection().id, 'collection')

        # we want the portlet to return us the same results as the collection
        self.assertEquals(collection_num_items, len(r.results()))

    def test_edit_link(self):
        collection = getattr(self.folder, 'collection')
        collection.setQuery(query)
        mapping = PortletAssignmentMapping()
        mapping['foo'] = carousel.Assignment(
            header=u"Test carousel",
            target_collection='/Members/test_user_1_/collection')
        r = self.renderer(context=None, request=None, view=None,
                          manager=None, assignment=mapping['foo'])
        self.assertTrue(r.editCarouselLink().endswith('/edit'))


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
