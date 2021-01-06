# LeetCode题解(0300)：最长上升子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-increasing-subsequence/)（中等）

标签：二分查找、贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (98.45%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        queue = []
        for num in nums:
            if not queue or queue[-1] < num:
                queue.append(num)
            else:
                idx = bisect.bisect_right(queue, num)
                if idx == 0 or (queue[idx - 1] != num):
                    queue[idx] = num
        return len(queue)
```

