# LeetCode题解(0438)：四数相加II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/4sum-ii/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 388ms (36.49%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（暴力哈希）：

```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        size = len(A)

        hashmap = collections.Counter()
        for i in range(size):
            for j in range(size):
                hashmap[A[i] + B[j]] += 1

        ans = 0
        for i in range(size):
            for j in range(size):
                ans += hashmap[-C[i] - D[j]]

        return ans
```