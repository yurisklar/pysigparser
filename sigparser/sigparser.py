import types
import parser_modules

class SignatureParser:
    """
    Parses text input to get information about a person
    """

    def __init__(self):
        
        self.parser_modules = [parser_modules.__dict__.get(mod) for mod in dir(parser_modules) if isinstance(parser_modules.__dict__.get(mod), types.ModuleType) and mod.startswith("look_for_")]

        print(self.parser_modules)
        
    def get_information(self, input):
        """
        returns the dictionary of parsed information
        """
        result = dict()

        for module in self.parser_modules:
            result = module.run(input, result)

        return result
