# LeetCode题解(1528)：重新排列字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shuffle-string/)（简单）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (46.84%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(indices)
        for i1, i2 in enumerate(indices):
            res[i2] = s[i1]
        return "".join(res)
```

