# LeetCode题解(1343)：大小为K且平均值大于等于阈值的子数组数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 156ms (50.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k

        now = 0
        for i in range(k):
            now += arr[i]

        ans = int(now >= threshold)

        for i in range(k, len(arr)):
            now += arr[i] - arr[i - k]
            if now >= threshold:
                ans += 1

        return ans
```

