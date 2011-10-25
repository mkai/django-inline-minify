from django import template
from minify.libs.jsmin import jsmin

register = template.Library()

class MinifyJs(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        return jsmin(self.nodelist.render(context))
        
@register.tag
def minify(parser, token):
    nodelist = parser.parse(('endminify',))
    parser.delete_first_token()
    return MinifyJs(nodelist)
