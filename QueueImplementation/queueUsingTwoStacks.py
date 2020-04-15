class QueueUsingTwoStacks:

    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self,data):#O(1)
        self.__s1.append(data)

    def dequeue(self):#O(n)
        if self.size() == 0:
            return -1
        while(self.size() != 1):
            self.__s2.append(self.__s1.pop())
        element = self.__s1.pop()
        while(len(self.__s2) != 0):
            self.__s1.append(self.__s2.pop())
        return element

    def front(self):
        if self.size() == 0:
            return -1
        return self.__s1[0]

    def size(self):
        return len(self.__s1)

    def isEmpty(self):
        return self.size() == 0

q = QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
while q.isEmpty() is False:
    print(q.dequeue())
print(q.front())
