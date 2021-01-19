# LeetCode题解(1031)：两个非重叠子数组的最大和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-sum-of-two-non-overlapping-subarrays/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 60ms (80.62%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxSumTwoNoOverlap(self, arr: List[int], s1: int, s2: int) -> int:
        size = len(arr)
        for i in range(1, size):
            arr[i] += arr[i - 1]

        ans, max1, max2 = arr[s1 + s2 - 1], arr[s1 - 1], arr[s2 - 1]

        for i in range(s1 + s2, size):
            max1 = max(max1, arr[i - s2] - arr[i - s1 - s2])  # 最后s2个留给s2，前面求s1最大值
            max2 = max(max2, arr[i - s1] - arr[i - s1 - s2])  # 最后s1个留给s1，前面求s2最大值
            ans = max(ans,
                      max1 + arr[i] - arr[i - s2],
                      max2 + arr[i] - arr[i - s1])

        return ans
```

