import heapq

array = [1,3,5,2,4]
heap = []
for num in array:
    heapq.heappush(heap,num)
    print("heap: ", heap)

print("array:", array)
heapq.heapify(array)
print("array:", array)

x = heapq.heappushpop(heap,6)
print("heap:",heap)
print("x:",x)

x = heapq.heapreplace(heap,7)
print("heap:",heap)
print("x:",x)

empty = []
heapq.heapify(empty)
heapq.heappushpop(empty,1)
print("empty: ",empty)
heapq.heapreplace(empty,1)
print("empty:",empty)