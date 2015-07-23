from collective.grok import gs
from samahan.site import MessageFactory as _

@gs.importstep(
    name=u'samahan.site', 
    title=_('samahan.site import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('samahan.site.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
