# LeetCode题解(0692)：前K个高频单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/top-k-frequent-words/)（中等）

标签：堆、排序、哈希表

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时      |
| -------------- | ------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(W+KlogW)$ | $O(W)$     | 64ms (91.39%) |
| Ans 2 (Python) |              |            |               |
| Ans 3 (Python) |              |            |               |

解法一（自定义堆排序）：

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        lst = heapq.nsmallest(k, count.keys(), key=lambda x: (-count[x], x))
        return lst
```