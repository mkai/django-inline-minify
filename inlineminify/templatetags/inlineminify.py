from django import template
from webassets.filter.jspacker.jspacker import JavaScriptPacker

register = template.Library()

class MinifyJs(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        return JavaScriptPacker().pack(self.nodelist.render(context), 
            compaction=False, encoding=62, fastDecode=True)

@register.tag
def inlineminify(parser, token):
    nodelist = parser.parse(('endinlineminify',))
    parser.delete_first_token()
    return MinifyJs(nodelist)
