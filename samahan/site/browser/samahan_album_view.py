from five import grok
from plone.directives import dexterity, form
from samahan.site.content.samahan_album import ISamahanAlbum

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ISamahanAlbum)
    grok.require('zope2.View')
    grok.template('samahan_album_view')
    grok.name('view')

