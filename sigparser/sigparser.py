import re

# changed the idea to use decorators
# because they would work here with input

class SignatureParser:
    """
    Parses text input to get information about a person
    """

    def __init__(self):
        self.regexps = dict(
            email = re.compile(r'([\w\-\.]+@[\w\-\.]+\.[\w\-]+)'),
            website = re.compile(r'(https?://[^\s]+)')
        )

    def get_information(self, input):
        result = dict()
        for look_for in self.regexps:
            matched = self.regexps[look_for].findall(input)
            if matched:
                result[look_for] = matched

        return result

