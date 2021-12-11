# Python heapq源码解读计划(四)

本文是解读python `heapq` 库的最后一节，主要分析的函数为`nlargest`和`nsmallest`这两个函数。

## nlargest函数的实现

`nlargest(n,iterable,key=None)`这个函数的功能为返回数据集中最大的n个元素，等价于`sorted(iterable, key=key, reverse=True)[:n]`。

#### n = 1时的处理
当` n = 1 `时，其实就是找出这个list中的最大值。这和使用`max()`函数是一样的，但是`max()`函数不接受空list，所以得想办法让heap为空的时候，返回一个空list，当heap不为空时，返回一个只有一个元素的list。

首先，需要利用python 的`iter()`函数来将list变成一个迭代器。
```python
it = iter(iterable)
```
然后生成一个空的`object()`，这个object()主要是用来处理后面空列表的情况。
```python
sentinel = object()
```

然后来判断key是否为None，最后利用max()函数获取结果。这里以`key=None`来说明：
```python
result = max(it, default=sentinel)
```
其实和普通的`max`使用类似，但是多了一个参数`default=sentinel`。加上这个参数的意义是当这个iter为空时，`max`返回的是一个object。最后只需要判断一下，如果result是sentinel，那么就返回一个空list，否则就返回`[result]`。

这部分的源码实现如下：

```python 
    if n == 1:
        it = iter(iterable)
        sentinel = object()
        if key is None:
            result = max(it, default=sentinel)
        else:
            result = max(it, default=sentinel, key=key)
        return [] if result is sentinel else [result]
```

测试：
```python
array = [1,3,2,4]
heap = []
print("heap:",heapq.nlargest(1,heap))
for num in array:
    heapq.heappush(heap,num)
    # print("heap: ", heap)
print("heap:",heapq.nlargest(1,heap))
```
结果:
```
heap: []
heap: [4]
```

#### 当n > size时

首先先来比较`n`和数组长度`size`哪个更大，如果`n >= size`，那么直接返回逆序排序的结果即可。


```python
    try:
        size = len(iterable)
    except (TypeError, AttributeError):
        pass
    else:
        if n >= size:
            return sorted(iterable, key=key, reverse=True)[:n]
```


#### 当 key 为 None时
当`n < size`时,所需要的做的事情就是找出来这个堆中最大的n个值。首先，和之前一样，利用python的`iter()`将`heap`变成了一个迭代器。然后从其中读取出两个元素。
```python
it = iter(iterable)
result = [(elem, i) for i, elem in zip(range(0, -n, -1), it)]
```
当`result`为空时，直接将`result`返回即可。
```python
if not result:
    return result
```
如果`result`不为空，则对`result`做一个`heapify`的处理，让其成为一个小根堆。然后提取出`result[0][0]`，令其为`top`，这个`top`为result中最小的值。
```python 
heapify(result)
top = result[0][0]
```

因为`it`是迭代器，而之前在构造`result`的时候已经获取了n个元素，所以在读取`it`中的元素的时候，是接着之前的读取的。当出现了`top`的值小于`elem`的值的时候，就说明`result`中的值并不是前n大的，所以需要利用`heapreplace`函数来将`elem`给换到`result`中去。

```python
_heapreplace = heapq.heapreplace
for elem in it:
    print("order:",order)
    print("elem:",elem)
    if top < elem:
        _heapreplace(result, (elem, order))
        print(result)
        top, _order = result[0]
        order -= 1
```

最后将`result`逆序排列一下，然后只拿出其中的elem来返回即可。

```python
result.sort(reverse=True)
return [elem for (elem, order) in result]
```

`order`的作用应该是为了分辨值相同的元素所带来的影响，即便值相同，但是`order`是不同的，可以利用`order`来将值相同的元素分辨出来。

#### General case
General case和key 为 None唯一的区别就是添加了key的元素其中。

#### nlargest整体代码：
```python
def nlargest(n, iterable, key=None):
    # Short-cut for n==1 is to use max()
    if n == 1:
        it = iter(iterable)
        sentinel = object()
        if key is None:
            result = max(it, default=sentinel)
        else:
            result = max(it, default=sentinel, key=key)
        return [] if result is sentinel else [result]

    # When n>=size, it's faster to use sorted()
    try:
        size = len(iterable)
    except (TypeError, AttributeError):
        pass
    else:
        if n >= size:
            return sorted(iterable, key=key, reverse=True)[:n]

    # When key is none, use simpler decoration
    if key is None:
        it = iter(iterable)
        result = [(elem, i) for i, elem in zip(range(0, -n, -1), it)]
        if not result:
            return result
        heapify(result)
        top = result[0][0]
        order = -n
        _heapreplace = heapreplace
        for elem in it:
            if top < elem:
                _heapreplace(result, (elem, order))
                top, _order = result[0]
                order -= 1
        result.sort(reverse=True)
        return [elem for (elem, order) in result]

    # General case, slowest method
    it = iter(iterable)
    result = [(key(elem), i, elem) for i, elem in zip(range(0, -n, -1), it)]
    if not result:
        return result
    heapify(result)
    top = result[0][0]
    order = -n
    _heapreplace = heapreplace
    for elem in it:
        k = key(elem)
        if top < k:
            _heapreplace(result, (k, order, elem))
            top, _order, _elem = result[0]
            order -= 1
    result.sort(reverse=True)
    return [elem for (k, order, elem) in result]
```

## nsmallest函数实现

`nsmallest`函数的整体实现和`nlargest`函数的实现是类似的。

#### n == 1时
这一部分的具体实现和`nlargerst`基本一样，只不过这里使用的是`min`函数

源码：
```python
if n == 1:
    it = iter(iterable)
    sentinel = object()
    if key is None:
        result = min(it, default=sentinel)
    else:
        result = min(it, default=sentinel, key=key)
    return [] if result is sentinel else [result]
```

#### 当n >= size时
这部分和`nlargest`函数一样。

#### 当 k 为 None时：
这里的结构也是和`nlargest`函数是一样的，但是有这么几点不同：

* `nlargest`函数中使用`heapify`的部分，这里使用的是`_heapify_max`。

* `nlargest`函数中使用`heapreplace`的部分，这里使用的是`_heapreplace_max`。

`_heapify_max`的作用其实就是构建一个大根堆。`_heapreplace_max`也是在大根堆中处理元素替代的问题。

源码：

```python
def nsmallest(n, iterable, key=None):
    """Find the n smallest elements in a dataset.

    Equivalent to:  sorted(iterable, key=key)[:n]
    """

    # Short-cut for n==1 is to use min()
    if n == 1:
        it = iter(iterable)
        sentinel = object()
        if key is None:
            result = min(it, default=sentinel)
        else:
            result = min(it, default=sentinel, key=key)
        return [] if result is sentinel else [result]

    # When n>=size, it's faster to use sorted()
    try:
        size = len(iterable)
    except (TypeError, AttributeError):
        pass
    else:
        if n >= size:
            return sorted(iterable, key=key)[:n]

    # When key is none, use simpler decoration
    if key is None:
        it = iter(iterable)
        # put the range(n) first so that zip() doesn't
        # consume one too many elements from the iterator
        result = [(elem, i) for i, elem in zip(range(n), it)]
        if not result:
            return result
        _heapify_max(result)
        top = result[0][0]
        order = n
        _heapreplace = _heapreplace_max
        for elem in it:
            if elem < top:
                _heapreplace(result, (elem, order))
                top, _order = result[0]
                order += 1
        result.sort()
        return [elem for (elem, order) in result]

    # General case, slowest method
    it = iter(iterable)
    result = [(key(elem), i, elem) for i, elem in zip(range(n), it)]
    if not result:
        return result
    _heapify_max(result)
    top = result[0][0]
    order = n
    _heapreplace = _heapreplace_max
    for elem in it:
        k = key(elem)
        if k < top:
            _heapreplace(result, (k, order, elem))
            top, _order, _elem = result[0]
            order += 1
    result.sort()
    return [elem for (k, order, elem) in result]
```