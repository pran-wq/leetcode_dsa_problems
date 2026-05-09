# for c in "hello":
#     print(f"{c} → {ord(c)}")
# def is_annagram(s1,s2):
#     if len(s1)!= len(s2):
#         return False
#     return sorted(s1) == sorted(s2)
        
# print(is_annagram("listen","silent"))
def is_annagram(s1,s2):
    count = {}
    if len(s1)!= len(s2):
        return False
    for c in s1:
        
        count[c] =count.get(c,0)+1
        
    for c in s2:
        if c not in count:
            return False 
        count[c]-=1
        

        if count[c]<0:
            return False
    return True
print(is_annagram("evil","vile"))

        


   
    
