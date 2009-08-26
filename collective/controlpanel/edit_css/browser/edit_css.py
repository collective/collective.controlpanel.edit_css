
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.component.hooks import getSite
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate 

class EditCSS(BrowserView):

    template = ViewPageTemplateFile('edit_css.pt')
    default_text = u'/* DELETE THIS LINE AND PUT YOUR CUSTOM STUFF HERE */'

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
        try: 
            return skins.custom['ploneCustom.css'].document_src()
        except:
            id = 'ploneCustom.css'
            text = self.default_text
            content_type = 'text/html'
            obj=ZopePageTemplate(id,text,content_type)
            skins.custom._setObject(id,obj)
            return skins.custom['ploneCustom.css'].document_src()

    def setPloneCustom(self,text):
        site = getSite()
        skins = site.portal_skins
        skins.custom['ploneCustom.css'].pt_edit(text,'text/html')
