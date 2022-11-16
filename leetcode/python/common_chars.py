from collections import Counter
import re
def commonChars(words):
        result = Counter(words[0])
        for w in words[1:]:
            result &= Counter(w)

        return list(result.elements())

print(commonChars(["bella","label","roller"]))