from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
# from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from samahan.site import MessageFactory as _

from plone.directives import form as directivesform
from plone.formwidget.multifile import MultiFileFieldWidget
from plone.namedfile.field import NamedFile
from zope import schema
from zope.interface import Interface



# Interface class; used to define content-type schema.

class ISamahanAlbum(form.Schema, IImageScaleTraversable):
    """
    Album
    """
    directivesform.widget(files=MultiFileFieldWidget)
    files = schema.List(title=u'Files',value_type=NamedFile())
    pass

alsoProvides(ISamahanAlbum, IFormFieldProvider)
