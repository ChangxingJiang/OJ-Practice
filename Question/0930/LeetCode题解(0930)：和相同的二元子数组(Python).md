# LeetCode题解(0930)：和相同的二元子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-subarrays-with-sum/)（中等）

标签：哈希表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 304ms (81.07%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = collections.Counter({0: 1})

        ans = 0
        last = 0
        for n in A:
            last += n
            if last - S in count:
                ans += count[last - S]
            count[last] += 1

        return ans
```