# LeetCode题解(1754)：构造字典序最大的合并字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-merge-of-two-strings/)（中等）

标签：贪心算法

| 解法           | 时间复杂度  | 空间复杂度 | 执行用时      |
| -------------- | ----------- | ---------- | ------------- |
| Ans 1 (Python) | $O((AB)^2)$ | $O(1)$     | 96ms (87.79%) |
| Ans 2 (Python) |             |            |               |
| Ans 3 (Python) |             |            |               |

解法一：

```python
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        size1, size2 = len(word1), len(word2)

        ans = []

        i1, i2 = 0, 0
        while i1 < size1 and i2 < size2:
            if word1[i1:] > word2[i2:]:
                ans.append(word1[i1])
                i1 += 1
            else:
                ans.append(word2[i2])
                i2 += 1

        if i1 < size1:
            ans.append(word1[i1:])
        if i2 < size2:
            ans.append(word2[i2:])

        return "".join(ans)
```

