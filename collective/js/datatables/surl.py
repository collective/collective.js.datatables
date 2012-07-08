from Products.Five.browser import BrowserView
from json import dumps
from zope.i18nmessageid import MessageFactory
_ = MessageFactory("collective.js.datatables")


class Translations(BrowserView):
    """Translation URL"""

    def __call__(self):
        self.request.response.setHeader('X-Theme-Disabled', 'True')
        self.request.response.setHeader('Content-Type', 'text/plain')
        return dumps(self.translate())

    def translate(self):
        t = self.context.translate
        translated = {}
        msgids = self.msgids()
        for key in msgids:
            if key not in ('oPaginate', 'oAria'):
                translated[key] = t(msgids[key])

        translated['oPaginate'] = {}
        for key in msgids['oPaginate']:
            translated['oPaginate'][key] = t(msgids['oPaginate'][key])

        translated['oAria'] = {}
        for key in msgids['oAria']:
            translated['oAria'][key] = t(msgids['oAria'][key])

        return translated

    def msgids(self):
        return {
            "sEmptyTable": _(u"sEmptyTable",
                        default=u"No data available in table"),
            "sInfo": _(u"sInfo",
                        default=u"Showing _START_ to _END_ of _TOTAL_ entries"),
            "sInfoEmpty": _(u"sInfoEmpty",
                        default=u"Showing 0 to 0 of 0 entries"),
            "sInfoFiltered": _(u"sInfoFiltered",
                        default=u"(filtered from _MAX_ total entries)"),
            "sInfoPostFix": _(u"sInfoPostFix",
                        default=u""),
            "sInfoThousands": _(u"sInfoThousands",
                        default=u","),
            "sLengthMenu": _(u"sLengthMenu",
                        default=u"Show _MENU_ entries"),
            "sLoadingRecords": _(u"sLoadingRecords",
                        default=u"Loading..."),
            "sProcessing": _(u"sProcessing",
                        default=u"Processing..."),
            "sSearch": _(u"sSearch",
                        default=u"Search:"),
            "sUrl": _(u"sUrl",
                        default=u""),
            "sZeroRecords": _(u"sZeroRecords",
                        default=u"No matching records found"),
            "oPaginate": {
                "sFirst": _(u"sFirst", default=u"First"),
                "sLast": _(u"sLast", default=u"Last"),
                "sNext": _(u"sNext", default=u"Next"),
                "sPrevious": _(u"sPrevious", default=u"Previous"),
            },
            "oAria": {
                "sSortAscending": _(u"sSortAscending",
                        default=u"activate to sort column ascending"),
                "sSortDescending": _(u"sSortDescending",
                        default=u"activate to sort column descending")
            }
        }
