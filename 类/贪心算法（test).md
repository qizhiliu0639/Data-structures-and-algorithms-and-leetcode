## 贪心算法

记录一下时间：
2021.8.1
今天的lc周赛第二题是一道贪心算法题目

##### 贪婪法的基本步骤：

步骤1：从某个初始解出发；
步骤2：采用迭代的过程，当可以向目标前进一步时，就根据局部最优策略，得到一部分解，缩小问题规模；
步骤3：将所有解综合起来。



##### 5831. 你可以工作的最大周数
```python
def numberOfWeeks(self, milestones: List[int]) -> int:
    milestones.sort()
        
    front = sum(milestones[:-1])
    back = milestones[-1]
        
    if back > front+1:
        return front*2 + 1
    else:
        return back + front
```
这道题主要是两个情况，一个是整个数列中的最大值大于其他值的合。这种情况很好理解，最大值就是 rest * 2 + 1。
第二种情况是最大值小于其他值的合，这种情况下返回值应为整个数列的合。（至于为什么，这个我也还没想明白）


##### 1874. 两个数组的最小乘积和
```python
def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort(reverse=True)
    res = 0
    for i in range(len(nums1)):
        res+=nums1[i]*nums2[i]
    return res
```
这道题的思路很简单，就是两个list排序，一个正向排，一个反向排，然后求出乘积合。

##### 1689. 十-二进制数的最少数目
```python
def minPartitions(self, n: str) -> int:
    return int(max(n))
```
这道题的思路也很简单，就是看一下这个数里面单个数最大值。

This version is git test
