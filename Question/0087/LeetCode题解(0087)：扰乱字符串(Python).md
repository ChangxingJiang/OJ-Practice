# LeetCode题解(0087)：判断字符串B是否为字符串A的扰乱字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/scramble-string/)（困难）

标签：字符串、递归

| 解法           | 时间复杂度          | 空间复杂度               | 执行用时      |
| -------------- | ------------------- | ------------------------ | ------------- |
| Ans 1 (Python) | 最坏情况 : $O(2^N)$ | 最坏情况 : $O(log(2^N))$ | 40ms (98.65%) |
| Ans 2 (Python) |                     |                          |               |
| Ans 3 (Python) |                     |                          |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
```