# LeetCode题解(0465)：最优账单平衡(Python)

题目：[原题链接](https://leetcode-cn.com/problems/optimal-account-balancing/)（困难）

标签：回溯算法、图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 868ms (25.67%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.people = []
        self.count = collections.Counter()
        self.ans = 0

    def minTransfers(self, transactions: List[List[int]]) -> int:
        for a, b, money in transactions:
            self.count[a] += money
            self.count[b] -= money
        self.people = list(self.count.keys())
        # print(self.people, self.count)
        self.ans = len(transactions)
        self.dfs(0, 0)
        return self.ans

    def dfs(self, i1, step):
        # print(step, ":", i1, [(key, self.count[key]) for key in self.people])

        # 剪枝条件
        if step > self.ans:
            return

        while i1 < len(self.people) and self.count[self.people[i1]] == 0:
            i1 += 1

        if i1 == len(self.people):
            self.ans = min(self.ans, step)
            # print(step, ":", "FINAL", [(key, self.count[key]) for key in self.people])

        for i2 in range(i1 + 1, len(self.people)):
            start = self.people[i1]
            end = self.people[i2]
            # 仅处理符号相反的情况即可
            if self.count[start] * self.count[end] < 0:
                # v = self.count[start]
                # self.count[start] -= v
                # self.count[end] += v
                self.count[end] += self.count[start]
                self.dfs(i1 + 1, step + 1)
                # self.count[start] += v
                # self.count[end] -= v
                self.count[end] -= self.count[start]
```