import glob

from os.path import dirname, basename, isfile

modules = glob.glob(dirname(__file__)+"/*.py")
modules_set = [ basename(f)[:-3] for f in modules if isfile(f) if not f.endswith('__init__.py')]
__all__ = modules_set