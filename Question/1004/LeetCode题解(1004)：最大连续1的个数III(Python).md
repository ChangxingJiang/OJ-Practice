# LeetCode题解(1004)：最大连续1的个数III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-consecutive-ones-iii/)（中等）

标签：数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 660ms (71.58%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def longestOnes(self, array: List[int], k: int) -> int:
        left = right = 0
        ans = 0
        now = 0
        while right < len(array):
            if array[right] == 0:
                now += 1
            while now > k:
                if array[left] == 0:
                    now -= 1
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans
```

