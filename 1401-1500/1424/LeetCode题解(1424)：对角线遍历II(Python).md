# LeetCode题解(1424)：对角线遍历II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/diagonal-traverse-ii/)（中等）

标签：排序、数组

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×max(N))$ | $O(1)$     | 超出时间限制   |
| Ans 2 (Python) | $O(M×N)$      | $O(M×N)$   | 244ms (54.81%) |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), max(len(row) for row in nums)

        ans = []

        for d in range(n + m - 1):
            if d < m:
                i0, j0, num = d, 0, min(d + 1, n)
            else:
                i0, j0, num = m - 1, d - m + 1, min(n + m - 1 - d, m)

            for k in range(num):
                i1, j1 = i0 - k, j0 + k
                if j1 < len(nums[i1]):
                    ans.append(nums[i1][j1])

        return ans
```

解法二：

```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), max(len(row) for row in nums)

        table = [[] for _ in range(n + m - 1)]
        for i in range(m):
            for j in range(len(nums[i])):
                table[i + j].append(nums[i][j])

        ans = []
        for row in table:
            ans.extend(reversed(row))
        return ans
```

