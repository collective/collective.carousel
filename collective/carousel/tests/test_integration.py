"""This is an integration test. It uses PloneTestCase, but does not
use doctest syntax.

You will find lots of examples of this type of test in CMFPlone/tests, for 
example.
"""

import unittest
from collective.carousel.tests.base import CarouselTestCase

from Products.CMFCore.utils import getToolByName

class TestCarousel(CarouselTestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def test_skins_is_available(self):
        self.failUnless('carousel' in self.portal.portal_skins.objectIds())

    def test_js_available(self):
        jsreg = getattr(self.portal, 'portal_javascripts')
        script_ids = jsreg.getResourceIds()
        self.failUnless('jquery.tools.min.js' in script_ids)
        self.failUnless('carousel.js' in script_ids)        
        
    def test_css_available(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.failUnless('carousel.css' in stylesheets_ids)
        
    def test_skin_layer(self):
        self.skins = self.portal.portal_skins
        themes = self.skins.getSkinSelections()
        for theme in themes:
            path = self.skins.getSkinPath(theme)
            path = [x.strip() for x in path.split(',')]
            self.failUnless('carousel' in path)
            self.assertEqual(path[1], 'carousel')

    def test_view_available_for_collection(self):
        views = self.portal.portal_types.Topic.getAvailableViewMethods(None)
        self.failUnless('carousel_view' in views)
        
    def test_view_is_selectable(self):
        self.setRoles(('Manager',))
        topic_id = self.folder.invokeFactory('Topic', 'test-topic')
        topic = getattr(self.folder, 'test-topic')
        topic.setLayout('carousel_view')
        self.assertEqual(topic.getLayout(), 'carousel_view')
        
    # Keep adding methods here, or break it into multiple classes or
    # multiple files as appropriate. Having tests in multiple files makes
    # it possible to run tests from just one package:
    #
    #   ./bin/instance test -s example.tests -t test_integration_unit


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCarousel))
    return suite