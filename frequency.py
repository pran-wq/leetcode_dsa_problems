def find_first(s):
    freq ={}
    for c in s:
        freq[c] = freq.get(c,0)+1
    for i, c in enumerate(s):
        if freq[c] ==1:
            return f"{c} at {i} "
        
    return "every character comes more than once"
print(find_first("leetcode"))  
print(find_first("aabb"))     
print(find_first("pranav"))



# def is_annagram(s1,s2):
#     freq={}
#     for c in s1:
#         freq[c]=freq.get(c,0)+1
#     for c in s2:
#         freq[c]-=1
#         if freq[c]!=0:
#             return "not an annagram"
#     return "An annagram"
# print(is_annagram("evil","veil"))
# # print(is_annagram("aab", "bba"))  
# print(is_annagram("abc", "ab"))

