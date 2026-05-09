def remove_duplicates(s):
    stack =[]
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            stack.append(s[i])
    return ''.join(stack)
print(remove_duplicates("aaca"))