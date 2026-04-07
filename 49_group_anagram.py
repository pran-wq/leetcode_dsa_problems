# Group all anagrams together!

# words = ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

def group_anagrams(words):
    group ={}
    for word in words:
        key = "".join(sorted(word))
        if key not in group:
            group[key]=[]
        group[key].append(word)
    return list(group.values())
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
