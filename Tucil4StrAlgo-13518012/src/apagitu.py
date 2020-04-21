from algorithms.KMPAlgorithm import searchPatternInTextWithKMP
from algorithms.BoyerMooreAlgorithm import searchPatternInTextWithBM
from algorithms.Regex import searchPatternInTextWithRegex

pattern = "anjay"
text = "hebat bet njay"

print(searchPatternInTextWithBM(pattern, text))
print(searchPatternInTextWithKMP(pattern, text))
print(searchPatternInTextWithRegex(pattern, text))