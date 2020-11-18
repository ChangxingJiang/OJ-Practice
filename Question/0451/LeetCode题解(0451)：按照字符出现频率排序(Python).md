# LeetCode题解(0451)：按照字符出现频率排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-characters-by-frequency/)（中等）

标签：哈希表、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 128ms (5.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（自定义排序）：

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        return "".join(sorted(s, key=lambda x: (count[x], x), reverse=True))
```