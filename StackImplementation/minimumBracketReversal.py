import math
def minimumBracketReversal(s):
    stack = []
    if len(s) %2 != 0:
        return -1
    for bracket in s:
        if bracket == "{":
            stack.append('{')
        elif(len(stack)>0 and stack[-1] == '{' and bracket == '}'):
            stack.pop()
        else:
            stack.append('}')
    m,n=0,0
    for i in stack:
        if i == '{':
            n = n + 1
        if i == '}':
            m = m + 1
    return(math.ceil(m/2)+math.ceil(n/2))

s = input()
count = minimumBracketReversal(s)
print(count)
