# AVL Tree

## Definition

### Is a balanced BST:
#### For all nodes, the difference in height between left and right subtree is at least one:

#### Also known as the AVL Property

## Height

### Since AVL Tree is just a variant of BST
#### Operations similarly depend on height

### Important Question:
#### Given N nodes, what isi the worst (tallest) AVL Tree?

To build a valid AVL tree of height H, the samllest number of nodes is...?

Height 1 Minimal AVL tree require <strong>1 node</strong>

Height 2 Minimal AVL tree require <strong>2 node</strong>

Height 3 Minimal AVL tree require <strong>4 node</strong>

Height 4 Minimal AVL tree require <strong>7 node</strong>

so n(h) = 1+n(h-1)+ n(h-2)

N is the number of nodes in a AVL tree of height h
h = O(log<small>2</small>N) (even in the worst case)

# ROTATION MECHANISM

Right Rotation

```python
p.left = rotateRight(p.left)

def rotateRight(x):
    l = x.left
    if l == None:
        return x
    
    x.left = l.right
    l.right = x
    return l
```