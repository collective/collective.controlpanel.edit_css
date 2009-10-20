
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate

class EditCSS(BrowserView):

    template = ViewPageTemplateFile('edit_css.pt')
    default_text = u'/* DELETE THIS LINE AND PUT YOUR CUSTOM STUFF HERE */'
    customcss = 'ploneCustom.css'

    def __call__(self,*args,**kw):
        request = self.context.request
        form = request.form

        # XXX Help! There has to be a better way.
        contains = form.__contains__
        if contains('edit_css') and contains('submit'):
            if form['submit'] == 'Save':
                self.setPloneCustom(form['edit_css'])
        return self.template()

    def getPloneCustom(self):
        site = getSite()
        skins = site.portal_skins
        if self.customcss in skins.custom.objectIds():
            try:
                return skins.custom[self.customcss].document_src()
            except:
                raise Exception("It's not possible to manage the object %s. "
                    "Use '%s' instead."%(repr(skins.custom[self.customcss]),
                    "ZopePageTemplate"))
        else:
            id = self.customcss
            text = self.default_text
            content_type = 'text/html'
            obj=ZopePageTemplate(id,text,content_type)
            skins.custom._setObject(id,obj)
            return skins.custom[self.customcss].document_src()

    def setPloneCustom(self,text):
        site = getSite()
        skins = site.portal_skins
        obj = skins.custom[self.customcss]
        try:
            if hasattr(obj,'manage_edit'):
                # DTMLMethod
                obj.manage_edit(text,'text/html')
            else:
                # ZopePageTemplate
                obj.pt_edit(text,'text/html')
        except:
            raise Exception("It's not possible to update object %s. "
                "Use '%s' instead."%(repr(obj),"ZopePageTemplate"))
        self.updatePloneCSS()

    def updatePloneCSS(self):
        site = getSite()
        cssreg = getToolByName(site, 'portal_css', None)
        if cssreg is not None:
            stylesheet_ids = cssreg.getResourceIds()
            if self.customcss not in stylesheet_ids:
                cssreg.registerStylesheet(id=sheetId, enabled=True)
                cssreg.cookResources()
            else:
                cssreg.updateStylesheet(self.customcss, enabled = True)
                cssreg.cookResources()
