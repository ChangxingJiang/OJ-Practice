# LeetCode题解(0341)：扁平化嵌套列表迭代器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flatten-nested-list-iterator/)（中等）

标签：栈、设计

这道题相当程度上是阅读理解。

| 解法           | 时间复杂度                                 | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | 构造=$O(1)$ ; hasNext=$O(N)$ ; next=$O(1)$ | $O(N)$     | 72ms (93.90%) |
| Ans 2 (Python) |                                            |            |               |
| Ans 3 (Python) |                                            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            self.stack += self.stack.pop().getList()[::-1]
        return self.stack != []
```