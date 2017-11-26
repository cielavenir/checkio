from collections import Counter
import re
def popular_words(text, words):
    c=Counter(re.sub(r'[\.,]','',text).lower().split())
    return {e:c[e] for e in words}
