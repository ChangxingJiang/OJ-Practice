# LeetCode题解(0558)：四叉树交集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/)（中等）

标签：树、回溯算法、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(logN)$  | 68ms (86.05%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # 如果两边都是叶节点
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val | quadTree2.val, True, None, None, None, None)

        # 如果一边是叶节点，一边不是叶节点
        elif quadTree1.isLeaf:
            if quadTree1.val == 1:
                return quadTree1
            else:
                return quadTree2
        elif quadTree2.isLeaf:
            if quadTree2.val == 1:
                return quadTree2
            else:
                return quadTree1

        # 如果两边都不是叶节点
        else:
            topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
                    topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
```

