# lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict

def anagramms(lst):
    dict_ = defaultdict(list)    
    for word in lst:
        dict_[''.join(sorted(word))].append(word)
        
    return [x for x in dict_.values()]

# anagramms(lst)