"""
Signatures parser
"""
import types
import parser_modules

class SignatureParser:
    """
    Parses text input to get information about a person
    """

    def __init__(self):

        """
        We collect all the modules we have in parser_modules
        which will extract the data from input
        The module name should start with "look_for_"
        """
        self.parser_modules = [parser_modules.__dict__.get(mod) for mod in dir(parser_modules)
                               if isinstance(parser_modules.__dict__.get(mod), types.ModuleType)
                                    and mod.startswith("look_for_")]

    def get_information(self, input):
        """
        returns the dictionary of parsed information
        """
        result = dict()

        # call the function "run" of each parsing module
        for module in self.parser_modules:
            result = module.run(input, result)

        return result
