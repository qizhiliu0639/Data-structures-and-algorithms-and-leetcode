# Python Collections 探索

参考文档：https://docs.python.org/3/library/collections.html

本文档的目的是学习并了解 Python Collections都有哪些数据结构，以及这些数据结构可以如何运用，以及他们的源码构成。通过学习这些了解当我们要设计一个新的数据结构的时候，该如何进行操作以及要注意哪些问题，还能学习python这门语言一些偏低层的内容。

# ChainMap objects

ChainMap提供了一个快速链接多个映射的类，可以将多个元素组合成一个单元。这比创建新字典并多次调用update()方法。

基础案例：

```python
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
list(ChainMap(adjustments, baseline))

output:
['music', 'art', 'opera']
```

## **maps**
ChainMap的maps方法会返回一个list，这个list里面会包含ChainMap中所有的map。

```python
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
c = ChainMap(baseline, adjustments)
print(c.maps)

output:
[{'music': 'bach', 'art': 'rembrandt'}, {'art': 'van gogh', 'opera': 'carmen'}]
```

## **new_child(m=None,** ****kwargs)**
使用new_child方法会构建一个新的ChainMap。

```python
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
c = ChainMap(baseline, adjustments)
d = c.new_child({'a' : 'b'})
e = c.new_child({'c' : 'd'})
print(c)
print(d)
print(e)

output:
ChainMap({'music': 'bach', 'art': 'rembrandt'}, {'art': 'van gogh', 'opera': 'carmen'})
ChainMap({'a': 'b'}, {'music': 'bach', 'art': 'rembrandt'}, {'art': 'van gogh', 'opera': 'carmen'})
ChainMap({'c': 'd'}, {'music': 'bach', 'art': 'rembrandt'}, {'art': 'van gogh', 'opera': 'carmen'})
```
从示例可以看出来，e和d都是继承了c这条父链，但是e和d之间是没有什么关系的。

## **parents**

返回一个新链，新链不包含ChainMap的maps中的第一个，可以类比成ChainMap(*d.maps[1:])。

```python
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
c = ChainMap(baseline, adjustments)
d = c.new_child({'a' : 'b'})
print(c.parents)
print(d.parents)

output:
ChainMap({'art': 'van gogh', 'opera': 'carmen'})
ChainMap({'music': 'bach', 'art': 'rembrandt'}, {'art': 'van gogh', 'opera': 'carmen'})
```



# Counter objects

Counter的作用是返回一个dict，将你提供的元素计数，并返回一个计数后的dict。

```python
Counter("abs")

>>> Counter({'a' : 1, 'b' : 1, 'c' : 1})

```

## Counter的一些方法：

## **element()**

Counter会自动过滤掉值小于1的元素。
```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

```
## **most_common([n])**

```python
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]
```

## **subtract([iterable-or-mapping])**

```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```

## **total()**
计算总共有多少个元素。
```python
>>> c = Counter(a=10, b=5, c=0)
>>> c.total()
15
```
## **fromkeys(iterable)**

## **update([iterable-or-mapping])**

# deque objects


# defaultdict objects


# namedtuple


# OrderedDict