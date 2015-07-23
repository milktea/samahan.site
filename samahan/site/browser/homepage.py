from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from Products.CMFCore.interfaces import ISiteRoot

grok.templatedir('templates')

class homepage(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def events(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.getPhysicalPath())
        results=[]
        brains = catalog.searchResults(path={'query':path, 'depth':1}, portal_type='Event', sort_on='Date', sort_order='reverse')[:3]
        
        return brains

    def albums(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.getPhysicalPath())
        results=[]
        brains = catalog.searchResults(path={'query':path, 'depth':1}, portal_type='samahan.site.samahanalbum', sort_on='Date', sort_order='reverse')[:10]
        for brain in brains:
            obj = brain._unrestrictedGetObject()
            results.append({'title': brain.Title,
                            'path': brain.getPath(),
                            'files': obj.files[:4]})
        return results

    def news_items(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.getPhysicalPath())
        results=[]
        brains = catalog.searchResults(path={'query':path, 'depth':1}, portal_type='News Item', sort_on='Date', sort_order='reverse')[:10]
        for brain in brains:
            results.append({'title': brain.Title,
                            'path': brain.getPath(),
                            'description': brain.description})
        return results