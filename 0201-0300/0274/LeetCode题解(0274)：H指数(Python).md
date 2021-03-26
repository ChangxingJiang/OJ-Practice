# LeetCode题解(0274)：H指数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/h-index/)（中等）

标签：排序、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 36ms (90.84%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i in range(len(citations)):
            ans = max(ans, min(i + 1, citations[i]))
            if citations[i] <= ans:
                break
        return ans
```