# LeetCode题解(0790)：多米诺和托米诺平铺(Python)

题目：[原题链接](https://leetcode-cn.com/problems/domino-and-tromino-tiling/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (83.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def numTilings(self, n: int) -> int:
        now = [1, 0, 0, 0]  # 两行均无空格，第1行空格，第2行空格，两行空格
        for _ in range(n):
            nxt = [0, 0, 0, 0]
            nxt[0] = (now[0] + now[1] + now[2] + now[3]) % self._MOD
            nxt[1] = (now[2] + now[3]) % self._MOD
            nxt[2] = (now[1] + now[3]) % self._MOD
            nxt[3] = (now[0]) % self._MOD
            now = nxt
        return now[0]
```

