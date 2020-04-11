from stackUsingArray import Stack

s = Stack()
s.push(10)
s.push(11)
s.push(12)

while s.isEmpty() is False:
    print(s.pop())
