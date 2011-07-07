from django import template
from jspacker import JavaScriptPacker

register = template.Library()

class MinifyJs(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        return JavaScriptPacker().pack(self.nodelist.render(context), 
            compaction=False, encoding=62, fastDecode=True)

def minifyjs(parser, token):
    nodelist = parser.parse(('endinlineminify',))
    parser.delete_first_token()
    return MinifyJs(nodelist)

minifyjs = register.tag(minifyjs)
