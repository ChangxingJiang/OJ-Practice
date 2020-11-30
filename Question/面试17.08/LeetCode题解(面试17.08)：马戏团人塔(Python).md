# LeetCode题解(面试17.08)：马戏团人塔(Python)

题目：[原题链接](https://leetcode-cn.com/problems/circus-tower-lcci/)（中等）

标签：排序、动态规划、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 320ms (67.22%) |
| Ans 3 (Python) |            |            |                |

解法一（暴力动态规划）：

```python
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        size = len(height)

        people = [(height[i], weight[i]) for i in range(size)]
        people.sort()

        # print(people)

        # 初始化状态表格
        dp1 = [1 for _ in range(size)]
        dp2 = [1 for _ in range(size)]

        # 状态转移计算
        for i in range(1, size):
            h1, w1 = people[i]
            dp2[i] = dp2[i - 1]
            for j in range(i - 1, -1, -1):
                h2, w2 = people[j]
                if h2 < h1 and w2 < w1:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
                    if dp2[j] < dp2[i] - 1:
                        break
            dp2[i] = max(dp2[i], dp1[i])

        # print(dp1)
        # print(dp2)

        return dp2[-1]
```

解法二（达到每个人数的最小体重动态规划）：

```python
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        size = len(height)

        people = [(height[i], -weight[i]) for i in range(size)]
        people.sort()

        weights = [-person[1] for person in people]

        # 求最大递增子序列
        dp = [float("inf") for _ in range(size)]

        for i in range(size):
            idx = bisect.bisect_left(dp, weights[i])
            # print(dp, weights[i], "->", idx)
            dp[idx] = min(dp[idx], weights[i])

        for i in range(size - 1, -1, -1):
            if dp[i] != float("inf"):
                return i + 1
```