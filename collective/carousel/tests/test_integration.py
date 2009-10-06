from zope.component import getUtility

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletType

from collective.carousel.tests.base import TestCase
from collective.carousel.browser.viewlets import CarouselViewlet
from collective.carousel.interfaces import ICarouselPortletsRow

class CarouselTestCase(TestCase):

    def test_carousel_layer_available(self):
        self.failUnless('carousel' in self.portal.portal_skins.objectIds())
        
    def test_carousel_layer_in_stack(self):
        self.skins = self.portal.portal_skins
        theme = self.skins.getDefaultSkin()
        path = self.skins.getSkinPath(theme)
        path = [x.strip() for x in path.split(',')]
        self.failUnless('carousel' in path)
        self.assertEqual(path[1], 'carousel')        

    def test_js_available(self):
        jsreg = getattr(self.portal, 'portal_javascripts')
        script_ids = jsreg.getResourceIds()
        self.failUnless('jquery.tools.min.js' in script_ids)
        self.failUnless('carousel.js' in script_ids)        

    def test_css_available(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.failUnless('carousel.css' in stylesheets_ids)
        
    def test_viewlet_is_available(self):
        request = self.app.REQUEST
        self.setRoles(['Manager', 'Member'])
        self.portal.invokeFactory('Folder', 'f1')
        context = getattr(self.portal, 'f1')
        viewlet = CarouselViewlet(context, request, None, None)
        self.failUnless(viewlet) 
        
    def test_portlet_manager_installed(self):
        manager = getUtility(IPortletManager, name=u"carousel.row")
        self.failUnless(ICarouselPortletsRow.providedBy(manager))
        
    def test_portlet_type_registered(self):
        portlet = getUtility(IPortletType, name='portlet.Carousel')
        self.assertEquals(portlet.addview, 'portlet.Carousel')        
        
    def test_collections_carouselable(self):
        from collective.carousel.interfaces import ICarouselable
        self.setRoles('Manager',)
        self.folder.invokeFactory("Topic", "test-collection")
        carouselable_col = getattr(self.folder, 'test-collection')
        self.failUnless(ICarouselable.providedBy(carouselable_col))

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)