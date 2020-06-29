def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"

def keypad(n):
    if n == 0:
        output = []
        output.append("")
        return output
    smallN = n//10
    lastDigit = n%10
    smallOutput = keypad(smallN)
    output = []
    options = getString(lastDigit)
    for s in smallOutput:
        for c in options:
            option = s + c
            output.append(option)
    return output

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)