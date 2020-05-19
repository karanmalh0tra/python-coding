import heapq
li = [1,5,4,8,7,9,11]
heapq.heapify(li)
print(li)
heapq.heappush(li,2)
print(li)
print(heapq.heappop(li))

heapq.heapreplace(li,6)
