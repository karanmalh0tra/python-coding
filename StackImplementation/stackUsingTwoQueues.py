
import queue
class StackUsingQueues:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()


    def push(self,data):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def getSize(self):
        pass

s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        while s.q1.qsize() !=0:
            print(s.q1.get(),end=' ')

    i+=1
