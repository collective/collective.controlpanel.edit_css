from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate


class EditJS(BrowserView):

    template = ViewPageTemplateFile('edit_css.pt')
    default_text = u'/* DELETE THIS LINE AND PUT YOUR CUSTOM STUFF HERE */'
    custom_js = 'ploneCustom.js'

    def __call__(self, *args, **kw):
        request = self.context.request
        form = request.form

        # XXX Replace this with Zope 2 form processing
        # http://docs.zope.org/zope2/zope2book/ScriptingZope.html#passing-parameters-to-scripts

        contains = form.__contains__
        if contains('edit_js') and contains('submit'):
            if form['submit'] == 'Save':
                self.setPloneCustom(form['edit_js'])
        return self.template()

    def getPloneCustom(self):
        site = getSite()
        skins = site.portal_skins
        if self.custom_js in skins.custom.objectIds():
            try:
                return skins.custom[self.custom_js].document_src()
            except:
                raise Exception("It's not possible to manage the object %s. "
                    "Use '%s' instead." % (repr(skins.custom[self.custom_js]),
                    "ZopePageTemplate"))
        else:
            id = self.custom_js
            text = self.default_text
            content_type = 'text/html'
            obj = ZopePageTemplate(id, text, content_type)
            skins.custom._setObject(id, obj)
            return skins.custom[self.custom_js].document_src()

    def setPloneCustom(self, text):
        site = getSite()
        skins = site.portal_skins
        obj = skins.custom[self.custom_js]
        try:
            if hasattr(obj, 'manage_edit'):
                # DTMLMethod
                obj.manage_edit(text, 'text/html')
            else:
                # ZopePageTemplate
                obj.pt_edit(text, 'text/html')
        except:
            raise Exception("It's not possible to update object %s. "
                "Use '%s' instead." % (repr(obj), "ZopePageTemplate"))
        self.updatePloneCustom()

    def updatePloneCustom(self):
        site = getSite()
        jsreg = getToolByName(site, 'portal_javascripts', None)
        if jsreg is not None:
            stylesheet_ids = jsreg.getResourceIds()
            if self.custom_js not in stylesheet_ids:
                jsreg.registerStylesheet(id=sheetId, enabled=True)
                jsreg.cookResources()
            else:
                jsreg.updateScript(self.custom_js, enabled=True)
                jsreg.cookResources()

