import json
from sigparser.sigparser import SignatureParser

class RequestHandler:

    def __init__(self):
        self._SigParser = SignatureParser()

    def parse_signature(self, input_text):
        return json.dumps(self._SigParser.get_information(input_text))

