# LeetCode题解(0932)：漂亮数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/beautiful-array/)（中等）

标签：分治算法、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 52ms (30.77%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N <= 2:
            return [i for i in range(1, N + 1)]
        else:
            d, r = divmod(N, 2)
            a, b = d + r, d
            res1 = self.beautifulArray(a)
            res2 = self.beautifulArray(b)
            res1 = [n * 2 - 1 for n in res1]
            res2 = [n * 2 for n in res2]
            return res1 + res2
```

