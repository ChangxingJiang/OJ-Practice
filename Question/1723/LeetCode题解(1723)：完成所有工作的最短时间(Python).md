# LeetCode题解(1723)：完成所有工作的最短时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/)（困难）

标签：回溯算法、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(N)$     | 72ms (79.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.jobs = []
        self.ans = 0
        self.k = 0
        self.avg = 0

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 处理工人比工作多的情况
        if k >= len(jobs):
            return max(jobs)

        # 处理只有一个工人的情况
        if k == 1:
            return sum(jobs)

        jobs.sort(reverse=True)

        # 处理工人比工作少1个的情况：工人至少有2个，工作至少有3个
        if k > 1 and k == len(jobs) - 1:
            return max(jobs[0], self.minimumTimeRequired(jobs[-2:], 1))

        # 处理工人比工作少2个的情况：工人至少有2个，工作至少有4个
        if k > 2 and k == len(jobs) - 2:
            return max(jobs[0], self.minimumTimeRequired(jobs[-4:], 2))

        # 处理工人比工作少3个的情况：工人至少有3个，工作至少有6个
        if k > 3 and k == len(jobs) - 3:
            return max(jobs[0], self.minimumTimeRequired(jobs[-6:], 3))

        # 处理工人比工作少4个的情况：工人至少有4个，工作至少有8个
        if k > 4 and k == len(jobs) - 4:
            return max(jobs[0], self.minimumTimeRequired(jobs[-8:], 4))

        # 处理工人比工作少5个的情况：工人至少有5个，工作至少有10个
        if k > 5 and k == len(jobs) - 5:
            return max(jobs[0], self.minimumTimeRequired(jobs[-10:], 5))

        self.jobs = jobs
        self.ans = sum(jobs)
        self.k = k
        self.avg = sum(jobs) // k

        self.dfs(idx=0, people=[0] * k, max_val=0)

        return self.ans

    def dfs(self, idx, people, max_val):
        # 处理递归完成的情况
        if idx == len(self.jobs):
            self.ans = min(self.ans, max_val)
            return

        # 剪枝条件1:处理已经不会有更优解的情况
        if max_val >= self.ans:
            return

        for i in range(self.k):
            # 剪枝条件2:处理当前位置已经超出平均值，不适合继续放置的情况
            if people[i] <= self.avg:
                people[i] += self.jobs[idx]
                self.dfs(idx + 1, people, max(max_val, people[i]))
                people[i] -= self.jobs[idx]
```

