from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from Testing import ZopeTestCase as ztc
from zope.interface import Interface


@onsetup
def setup_product():
    """Set up additional products and ZCML required to test this product.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    # Load the ZCML configuration for this package and its dependencies

    fiveconfigure.debug_mode = True
    from collective import carousel
    zcml.load_config('testing.zcml', package=carousel)
    fiveconfigure.debug_mode = False

    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML.

    ztc.installPackage('collective.carousel')


class ICustomType(Interface):
    """Custom helping interface for testing purposes only!
       Used to provide custom tile registration. Doing this with zcml for real
       is painful since custom zcml registration leaks to the following tests
       lower in the stack. Most probably you never want to use such marker
       interface in real-life implementation and would register your custom
       tile to either IATContentType (tile default for all types) or any
       specific interface like IATNewsItem
    """
    pass


# The order here is important: We first call the deferred function and then
# let PloneTestCase install it during Plone site setup

setup_product()
ptc.setupPloneSite(products=['collective.carousel'])
