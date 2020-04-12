class Stack:
    def __init__(self):
        self.__data = []
    def push(self,item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            return
        return self.__data.pop()
    def top(self):
        if self.isEmpty():
            return
        return self.__data[len(self.__data)-1]
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size() == 0


def checkBalanced(expr):
    brackets = {
    '}': '{',
    ')': '(',
    ']': '['
    }
    s = Stack()
    for element in expr:
        if element in brackets.values():
            s.push(element)
        elif element in brackets.keys():
            if s.top() == brackets[element]:
                s.pop()
            else:
                return False
    if s.size() == 0:
        return True
    else:
        return False

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')
