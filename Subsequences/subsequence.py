

def subsequences(string):
    if len(string) == 0:
        arr = []
        arr.append("")
        return arr
    smallerString = string[1:]
    smallArr = subsequences(smallerString)
    arr = []
    for sub in smallArr:
        arr.append(sub)
    for sub in smallArr:
        arr.append(string[0] + sub)
    
    return arr


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)