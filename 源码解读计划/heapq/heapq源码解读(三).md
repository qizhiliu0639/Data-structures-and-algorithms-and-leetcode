# Python heapq源码解读计划(三)
本文是解读`heapq`的第三节，主要来讲解一下`heappop`、`heappush`、`heappushpop`、`heapreplace`这四个个函数的具体实现。

## heappop函数的实现

`heappop`这个函数的具体作用为将`heap`内的最小值pop掉，并且返回这个最小值，与此同时这个heap还是保持在最小堆的状态。

首先，heapq的堆使用`list`来实现的，所以list可以执行的操作在这里也是可以使用的。

```python
lastelt = heap.pop()
```
所以`heappop`的源码会使用pop这个函数，先将一个值给踢掉。这个时候要保存住这个pop的值。如果pop完了这个`heap`为空了，那么直接返回pop的值即可。如果pop掉值后`heap`不为空，那么之前pop的值并不是`heap`中的最小值，所以需要将这个pop的值换为最小的值，也就是`heap[0]`。因为之前pop的值并不确定是否为剩余值中的最小值，所以使用`_siftup(heap,0)`来对这个`heap`进行一次调整。使其依旧为一个小根堆。

`_siftup()`的解读具体要看[heapq源码解读计划（二）](https://blog.csdn.net/qq_37511129/article/details/121846439?spm=1001.2014.3001.5501)

这部分的代码实现如下：
```python 
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup(heap, 0)
        return returnitem
```
整体的代码实现如下：

```python
def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
```

## heappush函数的实现

`heappush(heap,x)`这个函数的主要作用为将`x`的值添加到`heap`中去，并将heap保持在一个小根堆的状态。将`x`添加到`heap`中用到的是`list`的append的方法：

```python
heap.append(item)
```

然后使用`_siftdown`函数来将新append进去的值来与前面的叶节点值进行比较，如果比之前的值小，则进行一个交换，否则就会停止交换。

整体的`heappush`实现如下：

```python
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
```

## heapreplace函数的实现

函数英文描述如下：
>Pop and return the current smallest value, and add the new item.

具体来说就是先将最小值pop掉，然后再添加进去新值，最后要保持`heap`处于一个小根堆的状态。

`heapreplace(heap,x)`函数实现的功能为先将`x`的值和`heap`中的最小值进行一个交换，然后保持

具体的实现为先将`heap[0]`的值赋给`returnitem`，然后再将`x`的值赋给`heap[0]`。然后因为这是将值添加在了头部，所以是要用`_siftup`来对数组进行一个处理。最后将`returnitem`返回即可。

`heapreplace`的源码如下：
```python
def heapreplace(heap, item):
    returnitem = heap[0]    # raises appropriate IndexError if heap is empty
    heap[0] = item
    _siftup(heap, 0)
    return returnitem
```

## heappushpop函数的实现
`heappushpop(heap,x)`函数实现的是先将`x`的值添加到`heap`中去，然后再pop掉堆中最小的值。

如果`heap`是空的，或是`heap[0]`的值大于`x`的值，那么无需处理，直接将`x`的值pop掉即可。在代码上的实现为判断一下，如果是上述情况的话，`heap`无需处理，直接将`x`的值返回即可。

如果`heap[0]`的值小于`x`的值，那么将`x`的值和heap[0]的值进行互换，然后`_siftup`一下即可。

具体代码实现：
```python
def heappushpop(heap, item):
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _siftup(heap, 0)
    return item
```