from collective.carousel.tests.base import TestCase
from collective.carousel.browser.viewlets import CarouselViewlet

class ViewletTestCase(TestCase):
    
    def test_viewlet_is_available(self):
        request = self.app.REQUEST
        context = self.folder
        viewlet = CarouselViewlet(context, request, None, None)
        self.failUnless(viewlet)
        
    def test_viewlet(self):
        self.setRoles('Manager')       
        self.folder.invokeFactory('Topic', 'collection')
        
        crit = self.folder.collection.addCriterion('portal_type', 'ATSimpleStringCriterion')
        crit.setValue('Document')
        
        doc_ids = []
        # add a few documents
        for i in range(6):
            self.folder.invokeFactory('Document', 'document_%s'%i)
            doc_ids.append('document_%s'%i)
            getattr(self.folder, 'document_%s'%i).reindexObject()        
            
        collection_num_items = len(self.folder.collection.queryCatalog())
        # We better have some documents
        self.failUnless(collection_num_items >= 6)
        
        # we create a folder for test to not interfere with Documents in Collection results
        self.folder.invokeFactory('Folder', 'my-carousel', carouselprovider=(self.folder.collection,))
        carousel_obj = getattr(self.folder, 'my-carousel')
        field = carousel_obj.Schema().getField('carouselprovider')
        # technically the following checkup is done in test_field, but we better check again
        self.assertEqual(field.get(carousel_obj), self.folder.collection)
        
        viewlet = CarouselViewlet(carousel_obj, self.app.REQUEST, None, None)

        # first check provider()
        self.assertEqual(viewlet.provider(), self.folder.collection)
        
        # check results()
        self.failUnless(len(viewlet.results()) >= 6)
        results = [result.id for result in viewlet.results()]
        for doc_id in doc_ids:
            self.failUnless(doc_id in results)
        
        

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)