# from collections import Counter
# s = "programming"
# freq = Counter(s)
# print(freq.most_common(3))
# print("\n all the frequecies")
# for char, count in freq.items():
#     print(f"{char} : {count}")
def group_annagrams(words):
    group = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in group:
            group[key]= []
        group[key].append(word)
    return list(group.values())
words = ["eat","tea","tan","ate","nat","bat"]
print(group_annagrams(words))

