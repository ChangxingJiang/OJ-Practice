# LeetCode题解(0869)：重新排序得到2的幂(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reordered-power-of-2/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 40ms (79.39%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _BIG = 10 ** 9

    def reorderedPowerOf2(self, N: int) -> bool:
        aim = set()

        now = 1
        while now < min(self._BIG, N * 10):
            lst = [0] * 10
            for ch in str(now):
                lst[int(ch)] += 1
            aim.add(tuple(lst))
            now *= 2

        lst = [0] * 10
        for ch in str(N):
            lst[int(ch)] += 1
        return tuple(lst) in aim
```

