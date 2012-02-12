"""
Loader of available modules

Here we export all the modules in the directory
to be able to use them right away with
import parser_modules

This is done to have the possibility to just add new look_for_....py
and automatically add parsing and extracting one more entity from signature.
"""
import pkgutil

__all__ = []
for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    exec('%s = module' % module_name)