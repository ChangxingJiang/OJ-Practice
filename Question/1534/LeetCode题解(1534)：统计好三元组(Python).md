# LeetCode题解(1534)：统计数组中满足指定条件的三元组数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-good-triplets/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 1020ms (8%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一（暴力解法）：

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    d1, d2, d3 = abs(arr[i] - arr[j]), abs(arr[j] - arr[k]), abs(arr[i] - arr[k])
                    if d1 <= a and d2 <= b and d3 <= c:
                        ans += 1

        return ans
```