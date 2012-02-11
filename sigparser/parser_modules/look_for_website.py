import re

webpage_regexp = re.compile(r'(https?://[^\s]+)', re.IGNORECASE)

def run(input, output):
    matched = webpage_regexp.findall(input)
    if matched:
        output["website"] = matched
    return output