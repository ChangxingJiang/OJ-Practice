# LeetCode题解(1654)：到家的最少跳跃次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/)（中等）

标签：广度优先搜索、动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(6000)$  | $O(6000)$  | 92ms (60.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _BIG = 6001

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited0 = set(forbidden)
        visited1 = set(forbidden)
        queue = collections.deque([(0, 0)])
        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == x:
                    return step
                if i + a < self._BIG and i + a not in visited0:
                    queue.append((i + a, 0))
                    visited0.add(i + a)
                if j == 0 and i - b >= 0 and i - b not in visited1:
                    queue.append((i - b, 1))
                    visited1.add(i - b)
            step += 1
        return -1
```

