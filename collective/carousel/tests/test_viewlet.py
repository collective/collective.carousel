# Carousel is rendered through a viewlet in IAboveContent
# using items provided by the carousel provider added to the context

# from Products.Five.viewlet.manager import ViewletManager
# from plone.app.viewletmanager.manager import OrderedViewletManager
# from plone.app.layout.viewlets.interfaces import IAboveContent
# from Products.Five.browser import BrowserView as View

from collective.carousel.tests.base import TestCase
from collective.carousel.browser.viewlets import CarouselViewlet

class ViewletTestCase(TestCase):
    
    def test_viewlet_is_available(self):
        request = self.app.REQUEST
        context = self.folder
        viewlet = CarouselViewlet(context, request, None, None)
        self.failUnless(viewlet)
        
    def test_multiple_providers(self):
        self.setRoles('Manager') 
        collections = []
        for i in range(3):              
            self.folder.invokeFactory('Topic', 'collection_%s'%i)
            collection = getattr(self.folder, 'collection_%s'%i)
            crit = collection.addCriterion('portal_type', 'ATSimpleStringCriterion')
            crit.setValue('Document')
            collections.append(collection)
        field = self.folder.Schema().getField('carouselprovider')
        field.set(self.folder, tuple(collections))

        viewlet = CarouselViewlet(self.folder, self.app.REQUEST, None, None)
        
        self.failUnless(len(viewlet.getProviders()) >= 3)             
        
    def test_viewlet(self): 
        self.setRoles('Manager')       
        self.folder.invokeFactory('Topic', 'collection')
        
        crit = self.folder.collection.addCriterion('portal_type', 'ATSimpleStringCriterion')
        crit.setValue('Document')
        
        # add a few documents
        for i in range(10):
            self.folder.invokeFactory('Document', 'document_%s'%i)
            getattr(self.folder, 'document_%s'%i).reindexObject()
              
        collection_num_items = len(self.folder.collection.queryCatalog())
        # We better have some documents
        self.failUnless(collection_num_items >= 10)
        
        # we create a folder for test to not interfere with Documents in Collection results
        self.folder.invokeFactory('Folder', 'my-carousel', carouselprovider=(self.folder.collection,))
        carousel_obj = getattr(self.folder, 'my-carousel')
        field = carousel_obj.Schema().getField('carouselprovider')
        # technically the following checkup is done in test_field, but we better check again
        self.assertEqual(field.get(carousel_obj), [self.folder.collection])
        
        viewlet = CarouselViewlet(carousel_obj, self.app.REQUEST, None, None)

        # first check getProviders()
        self.assertEqual(viewlet.getProviders(), [self.folder.collection])
        
        # check results(). We get not more than 7 items even though the collection returns >=7 
        # results, don't we?
        self.failUnless(len(viewlet.results(viewlet.getProviders()[0])) == 7)
        results = [result.id for result in viewlet.results(viewlet.getProviders()[0])]         
        doc_ids = [id for id in self.folder.contentIds()[:7] if 'document' in id]
        for doc_id in doc_ids:
            self.failUnless(doc_id in results)
    
    def test_edit_carousel_link(self):
        self.setRoles('Manager')       
        self.folder.invokeFactory('Topic', 'collection')
        self.folder.invokeFactory('Folder', 'my-carousel', carouselprovider=(self.folder.collection,))
        carousel_obj = getattr(self.folder, 'my-carousel')

        viewlet = CarouselViewlet(carousel_obj, self.app.REQUEST, None, None)
        carousel_criteria = self.folder.collection.absolute_url() + '/criterion_edit_form'
        self.assertEqual(viewlet.editCarouselLink(viewlet.getProviders()[0]), carousel_criteria)
                

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)