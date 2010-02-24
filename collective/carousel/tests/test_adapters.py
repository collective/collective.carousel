from collective.carousel.tests.base import TestCase
from collective.carousel.browser.viewlets import CarouselViewlet
        
from Products.Five import zcml
import collective.carousel

class ViewsTestCase(TestCase):
    
    def afterSetUp(self):
        self.setRoles('Manager')       
        self.folder.invokeFactory('Topic', 'collection')
        collection = getattr(self.folder, 'collection')
        
        crit = self.folder.collection.addCriterion('portal_type', 'ATSimpleStringCriterion')
        crit.setValue(['Document', 'News Item', 'Event'])
        
        field = self.folder.Schema().getField('carouselprovider')
        field.set(self.folder, collection)
        
        # add a few objects
        self.folder.invokeFactory('Document', 'carousel-doc')
        self.folder.invokeFactory('News Item', 'carousel-news-item')
        self.folder.invokeFactory('Event', 'carousel-event')        

    def test_ct_views(self):
        from zope.component import queryMultiAdapter
        zcml.load_config('testing.zcml', collective.carousel)
        
        # test tile for a Page
        obj = getattr(self.folder, 'carousel-doc')
        tile = queryMultiAdapter((obj, self.app.REQUEST), name="carousel-view")
        self.failUnless('PAGE' in tile(), obj)
        
        # test tile for a News Item
        obj = getattr(self.folder, 'carousel-news-item')
        tile = queryMultiAdapter((obj, self.app.REQUEST), name="carousel-view")
        self.failUnless('NEWS ITEM' in tile(), obj)
        
        # test tile for an Event. 
        # Since we don't have any special view registered for Event in
        # zcml we should get default view for an object of this content type
        obj = getattr(self.folder, 'carousel-event')
        tile = queryMultiAdapter((obj, self.app.REQUEST), name="carousel-view")
        self.failUnless('DEFAULT' in tile(), obj)  
        
        # test tile for a Page in a carousel portlet
        # since we don't have any special view for Page in the carousel portlet
        # we should get default tile for the carousel portlet that is the same 
        # as for a carousel in the viewlet
        obj = getattr(self.folder, 'carousel-doc')
        tile = queryMultiAdapter((obj, self.app.REQUEST), name="carousel-portlet-view")
        self.failUnless('<p>This is a DEFAULT tile</p>' in tile(), obj)        
        

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)