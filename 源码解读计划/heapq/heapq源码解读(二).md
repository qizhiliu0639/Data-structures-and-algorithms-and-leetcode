# Python heapq源码解读计划(一)

本文为解读heapq部分的第二节，主要是探索heapq中的heapify()函数具体是如何实现的。

## 前言

首先来回顾一下，heapq中的heap是如何构造的。python heapq的heap使用数组实现，从0开始计数。对于所有的k,
都有 heap[k] <= heap[2 * k+1] 和 heap[k] <= heap[2 * k + 2]。


## 源码解读

### heapify(x)

源码：
```python 
def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)
```

heapify的源码其实很简单：
* 拿到数组的长度 n

* 取数组的中位数，然后从后往前遍历运行_siftup(x, i)

## _siftup(heap,pos)

源码：
```python
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
```
_siftup这个函数的作用为，将父节点的值和子节点中较小的节点进行交换，一直到没有子节点。子节点指的是heap[2k + 1] 和heap[2k + 2]。

然后执行_siftdown操作。

## _siftdown(heap,startpos,pos)

源码：
```python
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```

_siftdown作用就是从pos一直向上，如果节点值小于父节点，则进行交换，否则则break掉循环，终止执行。

