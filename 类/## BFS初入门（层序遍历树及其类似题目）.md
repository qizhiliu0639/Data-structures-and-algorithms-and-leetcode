## BFS初入门（层序遍历树及其类似题目）

之前看了很多网络博主写的BFS解题思想什么的，我觉得都不如直接来看题来的直接。BFS就是用队列的思想来实现的。我本身对这个没什么概念，近期翻看《算法图解》的时候看到了里面的讲解，才对这个思想有了一个初步的理解。

我选用了层序遍历树这道题作为例子，是因为我觉得这道题比较经典，我在看完《算法图解》后第一时间能想到的题目就是这个题目。我是使用的循环方法而非递归的方法。

大致的思路就是用while循环，当队列的queue list不为空时就一直循环下去。然后在每一次循环中我们都要用当前queue中的节点的子节点创建新的queue队列用于替换while中的queue，模拟出队列的那种FIFO的感觉。这样每次while的queue所代表的其实是树的每一层中的节点。

当然了，我觉得光看文字是不够的，不如多看看代码来理解。

#### 层序遍历二叉树
<https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/submissions/>
题目描述：
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

```python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        r = []
        queue_t = []
        for node in queue:
            r.append(node.val)
            if node.left != None:
                queue_t.append(node.left)
            if node.right != None:
                queue_t.append(node.right)
        res.append(r)
        queue = queue_t
    return res
```

层序遍历二叉树明白了以后，我觉得很多题做起来都不会有太大的问题了。
譬如：
#### 二叉树的层序遍历 II
<https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/>

#### N 叉树的层序遍历
<https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/>

#### 二叉树的右视图
<https://leetcode-cn.com/problems/binary-tree-right-side-view/>

#### 在每个树行中找最大值
<https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/>

#### 从上到下打印二叉树 III
<https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/>