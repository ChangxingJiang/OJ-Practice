# LeetCode题解(0282)：给表达式添加运算符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/expression-add-operators/)（困难）

标签：分治算法、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(4^N)$   | $O(N)$     | 7500ms (13.93%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一（极致暴力）：

```python
class Solution:
    def __init__(self):
        self.size = 0
        self.num = []
        self.now = []
        self.sign = []

    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []

        self.size = len(num)
        self.num = num
        self.now.append(num[0])
        self.dfs(0, num[0] == "0")

        ans = []
        for ss in self.sign:
            if eval(ss) == target:
                ans.append(ss)
        return ans

    def dfs(self, i, zero_start):
        if i == self.size - 1:
            self.sign.append("".join(self.now))
        else:
            # 递归+
            self.now.extend(["+", self.num[i + 1]])
            self.dfs(i + 1, self.num[i + 1] == "0")
            self.now.pop()
            self.now.pop()

            # 递归-
            self.now.extend(["-", self.num[i + 1]])
            self.dfs(i + 1, self.num[i + 1] == "0")
            self.now.pop()
            self.now.pop()

            # 递归*
            self.now.extend(["*", self.num[i + 1]])
            self.dfs(i + 1, self.num[i + 1] == "0")
            self.now.pop()
            self.now.pop()

            # 递归空
            if not zero_start:
                self.now.extend([self.num[i + 1]])
                self.dfs(i + 1, False)
                self.now.pop()
```

