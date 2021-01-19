# LeetCode题解(0853)：车队(Python)

题目：[原题链接](https://leetcode-cn.com/problems/car-fleet/)（中等）

标签：排序、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 192ms (84.97%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(position)
        lst = [(position[i], speed[i]) for i in range(size)]
        lst.sort(reverse=True)

        ans = 0
        last = 0
        for position, speed in lst:
            now = (target - position) / speed
            if now > last:
                ans += 1
            last = max(last, now)

        return ans
```

