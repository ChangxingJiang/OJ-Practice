# LeetCode题解(0364)：加权嵌套序列和II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/nested-list-weight-sum-ii/)（中等）

标签：深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (96.92%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = [[]]

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.dfs(nestedList, 0)

        ans = 0
        for i in range(len(self.ans)):
            height = len(self.ans) - i
            ans += height * sum(self.ans[i])
        return ans

    def dfs(self, lst, depth):
        if len(self.ans) < depth + 1:
            self.ans.append([])
        for elem in lst:
            if elem.isInteger():
                self.ans[depth].append(elem.getInteger())
            else:
                self.dfs(elem.getList(), depth + 1)
```