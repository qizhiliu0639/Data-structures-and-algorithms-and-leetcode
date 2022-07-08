# Python Collections 探索

参考文档：https://docs.python.org/3/library/collections.html

## ChainMap objects

ChainMap提供了一个快速链接多个映射的类，可以将多个元素组合成一个单元。这比创建新字典并多次调用update()方法。

基础案例：

```python
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
list(ChainMap(adjustments, baseline))

output:
['music', 'art', 'opera']
```


## Counter objects


## deque objects


## defaultdict objects


## namedtuple


## OrderedDict