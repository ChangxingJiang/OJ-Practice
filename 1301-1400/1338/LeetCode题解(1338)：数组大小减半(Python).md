# LeetCode题解(1338)：数组大小减半(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reduce-array-size-to-the-half/)（中等）

标签：数组、贪心算法、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 108ms (79.26%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        target = len(arr) // 2
        now = len(arr)

        ans = 0
        for num in sorted(count.values(), reverse=True):
            now -= num
            ans += 1
            if now <= target:
                break

        return ans
```

