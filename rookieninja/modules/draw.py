from jinja2 import Environment, FileSystemLoader, FileSystemBytecodeCache
from rookieninja import settings


bcc = FileSystemBytecodeCache(settings.JINJA2_CACHE, '%s.cache')
jinja2_env = Environment(
        loader=FileSystemLoader('templates/'), bytecode_cache=bcc)

def template(name, *args, **ctx):
    t = jinja2_env.get_template(name)
    return t.render(**ctx)