from Products.Five.testbrowser import Browser
from Testing.ZopeTestCase import Sandboxed
from Products.PloneTestCase import PloneTestCase as ptc
from collective.carousel import testing

ptc.setupPloneSite()


class TestCase(Sandboxed, ptc.PloneTestCase):
    """ Base class used for test cases """

    layer = testing.layer
    
class FunctionalTestCase(ptc.FunctionalTestCase):

    layer = testing.layer

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = Browser()
        if loggedIn:
            user = ptc.default_user
            pwd = ptc.default_password
            browser.addHeader('Authorization', 'Basic %s:%s' % (user, pwd))
        return browser