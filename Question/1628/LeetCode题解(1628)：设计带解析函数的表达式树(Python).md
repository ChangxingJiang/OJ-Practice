# LeetCode题解(1628)：设计带解析函数的表达式树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-an-expression-tree-with-evaluate-function/)（中等）

标签：设计、树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (75.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
from abc import ABC


class Node(ABC):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if not self.left and not self.right:
            return self.val
        else:
            mark = self.val
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()
            if mark == "+":
                return left_val + right_val
            elif mark == "-":
                return left_val - right_val
            elif mark == "*":
                return left_val * right_val
            else:
                return int(left_val / right_val)

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for t in postfix:
            if t.isnumeric():
                stack.append(Node(int(t)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(t, left, right))
        return stack.pop()
```