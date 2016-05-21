from bottle import get
from rookieninja.models.index import get_stats
from rookieninja.modules.draw import template


@get('/')
def index():
    return template('index.tpl', **{'stats': get_stats(True)})
