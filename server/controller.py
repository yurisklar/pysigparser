import json
from sigparser.sigparser import SignatureParser

class RequestHandler:
    """
    Controller class to handle XML-RPC calls
    """
    def __init__(self):
        self._SigParser = SignatureParser()

    def parse_signature(self, input_text):
        """
        receives the signature information using SignatureParser
        """
        return json.dumps(self._SigParser.get_information(input_text))

