# LeetCode题解(0339)：嵌套列表权重和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/nested-list-weight-sum/)（简单）

标签：深度优先搜索

| 解法           | 时间复杂度                             | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+D)$ : 其中N为数值总数,D为最大深度 | $O(D)$     | 44ms (45.54%) |
| Ans 2 (Python) |                                        |            |               |
| Ans 3 (Python) |                                        |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = 0

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        for lst in nestedList:
            self.dfs(lst, 1)
        return self.ans

    def dfs(self, lst, depth):
        if lst.isInteger():
            self.ans += depth * lst.getInteger()
        else:
            for lst in lst.getList():
                self.dfs(lst, depth + 1)
```