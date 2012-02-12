import re
import string

signature_statements = (
    "warm regards",
    "kind regards",
    "regards",
    "cheers",
    "many thanks",
    "thanks",
    "sincerely",
    "ciao",
    "best",
    "bGIF",
    "thank you",
    "thankyou",
    "talk soon",
    "cordially",
    "yours truly",
    "thanking You",
    "sent from my iphone"
)

person_name_regexp = re.compile(r'(' + string.join(signature_statements, "|") + ')[^\s]*\s([\w ]+)\s', re.IGNORECASE)

def run(input, output):
    matched = person_name_regexp.findall(input)
    if matched:
        output["name"] = matched[0][1]
    return output