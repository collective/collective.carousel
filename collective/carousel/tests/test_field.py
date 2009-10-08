# In these tests we are testing a ReferenceField injected to all 
# content types. The field has to accept objects, providing 
# content for carousel.
# 
# We accept only Collections in ATReferenceBrowserWidget of the field
# but in these tests we assume that widget itself works as it should 
# and doesn't allow to add objects of any other content type.

from collective.carousel.tests.base import TestCase

class FieldTestCase(TestCase):
        
    def test_field_available(self):
        # Test that we have a field on objects
        self.folder.invokeFactory('Document', 'my-page')
        new_obj = getattr(self.folder, 'my-page')
        # first test newly created document
        self.failUnless(new_obj.Schema().has_key('carouselprovider'))
        # now test the folder
        self.failUnless(self.folder.Schema().has_key('carouselprovider'))        

    def test_field_stored(self):
        # Whether we can change the field and the value of it is getting stored
        self.setRoles('Manager',)
        self.folder.invokeFactory("Topic", "test-collection")
        carouselable_col = getattr(self.folder, 'test-collection')
        self.folder.invokeFactory('Document', 'my-page', carouselprovider=(carouselable_col,))
        new_obj = getattr(self.folder, 'my-page')
        field = new_obj.Schema().getField('carouselprovider')
        # we deal with multiValued field, thus we are getting a list out of the field
        self.assertEqual(field.get(new_obj), [carouselable_col])

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)