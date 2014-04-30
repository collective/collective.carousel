# Testing basic integration of the package into Plone
from collective.carousel.tests.base import TestCase
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility


class CarouselTestCase(TestCase):

    def test_js_available(self):
        jsreg = getattr(self.portal, 'portal_javascripts')
        script_ids = jsreg.getResourceIds()
        self.failUnless('++resource++plone.app.jquerytools.plugins.js'
                        in script_ids)
        self.failUnless(
            '++resource++collective.carousel/carousel.js' in script_ids)

    def test_css_available(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.failUnless(
            '++resource++collective.carousel/carousel.css' in stylesheets_ids)

    def test_collections_carouselable(self):
        from collective.carousel.interfaces import ICarouselProvider
        self.setRoles('Manager', )

        self.folder.invokeFactory('Collection', 'test-collection')
        carouselable_col = getattr(self.folder, 'test-collection')
        self.failUnless(ICarouselProvider.providedBy(carouselable_col))

    def test_portlet_type_registered(self):
        portlet = getUtility(IPortletType, name='portlet.Carousel')
        self.assertEquals(portlet.addview, 'portlet.Carousel')


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
