import re

def searchPatternInTextWithRegex(pattern, text):
    return re.search(pattern, text) != None