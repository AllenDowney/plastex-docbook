#!/usr/bin/env python
from plasTeX.Renderers.PageTemplate import Renderer as _Renderer

class DocBook45(_Renderer):
    """ Renderer for DocBook Version 4.5 documents """
    fileExtension = '.xml'
    imageTypes = ['.png', '.jpg', '.jpeg', '.gif', '.pdf']
    vectorImageTypes = ['.svg']

    def cleanup(self, document, files, postProcess=None):
        res = _Renderer.cleanup(self, document, files, postProcess=postProcess)
        return res

    def processFileContent(self, document, s):
        s = _Renderer.processFileContent(self, document, s)
        return s
    
Renderer = DocBook45
