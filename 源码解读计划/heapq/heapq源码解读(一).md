# Python heapq源码解读计划(一)


## heapq的介绍与基本操作
（原文地址：https://docs.python.org/3/library/heapq.html#basic-examples）
这个库提供一个堆的算法实现，也称为优先队列算法。

#### 什么是堆
（这里使用的堆都是小根堆，也成为小顶堆）堆是二叉树，其每个父节点的值都小于或等于其任何子节点。为了方便比较，不存在的元素
都默认是无限大的。

#### API与教科书的差别

1. 使用从0开始的索引。这样会使节点的索引和其子节点的索引之间的关系稍微不那么明显，但更合适，因为python是用的从0开始的索引。
2. 这个库使用的是小根堆而不是大根堆。

#### 初始化
使用一个空列表来创建一个堆，或是使用heapify()来将一个非空列表转换为堆。

### heappush(heap,item)
heapq.heappush可以将值添加到heap中去。

Example：
```python
import heapq

array = [1,3,5,2,4]
heap = []
for num in array:
    heapq.heappush(heap,num)


print("array:", array)
print("heap: ", heap)
```

输出的结果
```
array: [1, 3, 5, 2, 4]
heap:  [1, 2, 5, 3, 4]
```

### heappop(heap)
将堆顶元素删除，如果堆为空，则会引发IndexError。返回删除的值。

Example:
```python
x = heapq.heappop(heap)
print("heap:",heap)
print("x:",x)
```
Result:
```
heap: [2, 3, 5, 4]
x: 1
```
### heappushpop(heap,item)

这是一套组合拳，将`item`添加到`heap`中去，然后将堆顶的元素删除，并返回这个被删除的值。

Example:
```python
x = heapq.heappushpop(heap,6)
print("heap:",heap)
print("x:",x)
```

Result:
```
heap: [2, 3, 5, 6, 4]
x: 1
```

### heapify(list):
在线性时间内将列表转换成堆。

Example:
```python
heapq.heapify(array)
print("array:", array)
```
Result:
```
array: [1, 2, 5, 3, 4]
```

### heapreplace(heap,item)

删除掉堆顶的元素，然后将新元素添加到堆中去。如果堆是空的，则会引发IndexError。

Example:
```python
x = heapq.heapreplace(heap,7)
print("heap:",heap)
print("x:",x)

empty = []
heapq.heapify(empty)
heapq.heappushpop(empty,1)
print("empty: ",empty)
heapq.heapreplace(empty,1)
print("empty:",empty)
```

Result:
```
heap: [3, 4, 5, 6, 7]
x: 2
empty:  []
Traceback (most recent call last):
  File "D:/Github/刷题心得/刷题心得指南/Source Code Project/heapq/heapqTest.py", line 25, in <module>
    heapq.heapreplace(empty,1)
IndexError: index out of range
```