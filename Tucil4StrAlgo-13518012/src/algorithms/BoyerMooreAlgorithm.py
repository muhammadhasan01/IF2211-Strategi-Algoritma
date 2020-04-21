# Declare constants
NUM_OF_CHAR = 256

def searchPatternInTextWithBM(pattern, text):
    # Preprocess bad character heuristic
    # Initialize all occurences with -1
    badChar = [-1 for _ in range(NUM_OF_CHAR)]

    # Filling the listed value with last occurences
    patLength = len(pattern)
    for i in range(patLength):
        badChar[ord(pattern[i])] = i
    
    # Search if there is the pattern in the text
    textLength = len(text)
    iterShift = 0
    while iterShift <= textLength - patLength:
        # set iterPattern to last index on pattern
        iterPattern = patLength - 1

        # keep reducing iterPattern when the characters are matching
        # in this iterShift
        while iterPattern >= 0 and pattern[iterPattern] == text[iterPattern + iterShift]:
            iterPattern -= 1
        
        # if the pattern occurs then iterPattern < 0
        if iterPattern < 0:
            # pattern found
            return True
        else:
            # shift the pattern
            iterShift += max(1, iterPattern - badChar[ord(text[iterPattern + iterShift])])
    
    # pattern not found
    return False

