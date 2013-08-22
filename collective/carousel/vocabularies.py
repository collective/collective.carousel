from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from plone.app.imaging.utils import getAllowedSizes


def ImageScaleVocabulary(context):
    allowed_sizes = getAllowedSizes()
    items = [(u'%s(%s, %s)' % (key, value[0], value[1]), key)
            for key, value in allowed_sizes.items() if allowed_sizes]
    return SimpleVocabulary.fromItems(items)

directlyProvides(ImageScaleVocabulary, IVocabularyFactory)
