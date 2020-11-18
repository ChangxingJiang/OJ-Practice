# LeetCode题解(面试01.02)：判断两个字符串是否为字符重排(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-permutation-lcci/)（简单）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1+N2)$ | 40ms (65.99%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return collections.Counter(s1) == collections.Counter(s2)
```