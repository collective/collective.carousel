import os.path

from collective.carousel.tests.base import TestCase
from collective.carousel.browser.viewlets import CarouselViewlet

class AdaptersTestCase(TestCase):
    
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
        
        from Products.Five import zcml
        zcml.load_string('''<configure xmlns="http://namespaces.zope.org/browser">
        <page
          name="carousel-view"                  
          for="Products.ATContentTypes.interface.IATContentType"
          template="default_tile.pt"
          permission="zope2.View"
          />
        <page
          name="carousel-view"                  
          for="Products.ATContentTypes.interface.IATNewsItem"
          template="news_item_tile.pt"
          permission="zope2.View"
          /> 
        <page
          name="carousel-view"                  
          for="Products.ATContentTypes.interface.IATDocument"
          template="page_tile.pt"
          permission="zope2.View"
          />                   
        </configure>''')
    
    def test_adapters(self):
        self.fail()
        
        

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)