
import queue



def reverseFirstK(q,k):
    stack = []
    n = q.qsize()
    for i in range(k):
        stack.append(q.get())
    while len(stack) != 0:
        q.put(stack.pop())
    for i in range(n-k):
        q.put(q.get())




from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k)
while(q.qsize()>0):
	print(q.get())
	n-=1
