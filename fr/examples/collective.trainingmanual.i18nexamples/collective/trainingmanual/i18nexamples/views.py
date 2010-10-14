from zope.interface import Interface
from zope.i18n import translate

from Products.Five import BrowserView

from collective.trainingmanual.i18nexamples import MyMessageFactory as _
from Products.CMFPlone import PloneMessageFactory as PMF

class I18nExampleView(BrowserView):

    def message(self):
        return _(u'my_message', default=u"Some words")

    def save(self):
        return PMF(u'Save')

    def map(self):
        msg_map = {'count': 12}
        return _(u'images_in_folder',
                 default=u"This folder has ${count} images",
                 mapping=msg_map)

    def translated(self):
        message = _(u'my_message', default=u"Some words")
        return translate(message, context=self.request)