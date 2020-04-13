def checkRedundant(string):
    s = []
    brackets = {']':'[',')':'(','}':'{'}
    for char in string:
        if char not in brackets.keys():
            s.append(char)
        else:
            count = 0
            while s[-1] != brackets[char]:
                s.pop()
                count = count + 1
            s.pop()
            if count == 0:
                return True
    return False




string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')
