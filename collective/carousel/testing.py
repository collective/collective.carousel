from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase.PloneTestCase import installPackage
from collective.testcaselayer.ptc import BasePTCLayer, ptc_layer


class Layer(BasePTCLayer):
    """ set up basic testing layer """

    def afterSetUp(self):
        # load zcml for this package and its dependencies
        fiveconfigure.debug_mode = True
        from collective import carousel
        zcml.load_config('testing.zcml', package=carousel)
        fiveconfigure.debug_mode = False
        # after which the required packages can be initialized
        installPackage('collective.carousel', quiet=True)
        # finally load the testing profile
        self.addProfile('collective.carousel:default')

layer = Layer(bases=[ptc_layer])
