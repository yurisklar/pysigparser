import re

# todo: not completed - use decorators

class SignatureParser:
    """
    Parses text input to get information about a person
    """

    def _get_website(self, input, result):
        result["URL"] = "http://example.com"
        return result

    def get_information(self, input):
        result = dict()
        result = self._get_website(input, result)
        return result
