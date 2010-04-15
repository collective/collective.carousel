from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase.PloneTestCase import installPackage
from collective.testcaselayer.ptc import BasePTCLayer, ptc_layer

from zope.interface import Interface

class ICustomType(Interface): 
    """Custom helping interface for testing purposes only! 
       Used to provide custom tile registration. Doing this with zcml for real is painful since
       custom zcml registration leaks to the following tests lower in the stack. Most probably you
       never want to use such marker interface in real-life implementation and would register your
       custom tile to either IATContentType (tile default for all types) or any specific interface
       like IATNewsItem
    """
    pass

class Layer(BasePTCLayer):
    """ set up basic testing layer """

    def afterSetUp(self):
        # load zcml for this package and its dependencies
        fiveconfigure.debug_mode = True
        from collective import carousel
        zcml.load_config('testing.zcml', package=carousel)
        zcml.load_config('custom_tile_testing.zcml', package=carousel)
        fiveconfigure.debug_mode = False
        # after which the required packages can be initialized
        installPackage('collective.carousel', quiet=True)
        # finally load the testing profile
        self.addProfile('collective.carousel:default')

layer = Layer(bases=[ptc_layer])
