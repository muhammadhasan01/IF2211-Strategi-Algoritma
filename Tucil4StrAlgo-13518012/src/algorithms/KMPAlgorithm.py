def searchPatternInTextWithKMP(pattern, text):
    # precompute longest prefix suffix of the pattern
    lps = [0]
    patLength = len(pattern)
    for i in range(1, patLength):
        j = lps[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        lps.append(j)
    
    # search if there is pattern in the text
    textLength = len(text)
    iterText = 0
    iterPattern = 0
    while iterText < textLength:
        # if current character in the pattern matches with text
        # increment both iter
        if text[iterText] == pattern[iterPattern]:
            iterText += 1
            iterPattern += 1

        if iterPattern == patLength:
            # pattern found
            return True
        # mismatch after iterPattern matches
        elif iterText < textLength and text[iterText] != pattern[iterPattern]:
            # use lps so we won't have to check every character
            if iterPattern > 0:
                iterPattern = lps[iterPattern - 1]
            else:
                iterText += 1

    # pattern not found
    return False