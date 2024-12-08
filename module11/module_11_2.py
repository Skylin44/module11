import inspect
import sys
import pprint

def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attributes'] = dir(obj)
    info['methods'] = inspect.getmembers(obj)
    info['module'] = inspect.getmodule(obj)
    return info

def sys_info():
    info = {}
    info['version'] = sys.version
    info['platform'] = sys.platform
    info['executable'] = sys.executable
    info['path'] = sys.path
    return info

pprint.pprint(introspection_info(42))
pprint.pprint(sys_info())
