from django import template
from ..lib.jsmin import jsmin
from ..lib.packer import JavaScriptPacker

register = template.Library()


class MinifyJsNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return jsmin(self.nodelist.render(context))


class JsPackerNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return JavaScriptPacker().pack(self.nodelist.render(context),
                                       encoding=62, fastDecode=True)


@register.tag
def minify(parser, token):
    try:
        tag_name, engine = token.split_contents()
    except ValueError:
        engine = 'jsmin'

    nodelist = parser.parse(('endminify',))
    parser.delete_first_token()

    if engine == 'jsmin':
        return MinifyJsNode(nodelist)
    elif engine == 'packer':
        return JsPackerNode(nodelist)
