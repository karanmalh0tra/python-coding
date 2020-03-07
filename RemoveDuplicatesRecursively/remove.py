def removeConsecutiveDuplicates(string):
    if len(string) == 0 or len(string) == 1:
        return string
    if string[0] == string[1]:
        smallOutput = removeConsecutiveDuplicates(string[1:])
        return smallOutput
    else:
        smallOutput = removeConsecutiveDuplicates(string[1:])
        return string[0] + smallOutput

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
