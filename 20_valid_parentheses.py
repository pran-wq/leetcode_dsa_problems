#20
def check_parentheses(bracket):
    stack=[]
    pairs = {
        ')':'(',
        '}':'{',
        ']':'['    }
    for char in bracket:
        if char in '[{(':
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            if stack.pop() != pairs[char]:
                return False
    return len(stack)==0
print(check_parentheses("[{()}]"))
