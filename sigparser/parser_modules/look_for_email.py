"""
module to extract Email information from signature
"""
import re

email_regexp = re.compile(r'([\w\-\.]+@[\w\-\.]+\.[\w\-]+)', re.IGNORECASE)

def run(input, output):
    matched = email_regexp.findall(input)
    if matched:
        output["email"] = matched
    return output