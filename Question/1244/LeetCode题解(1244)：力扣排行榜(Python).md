# LeetCode题解(1244)：力扣排行榜(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-a-leaderboard/)（中等）

标签：设计、哈希表、排序

| 解法           | 时间复杂度                    | 空间复杂度 | 执行用时      |
| -------------- | ----------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 插入 = $O(1)$ ; 查询 = $O(N)$ | $O(N)$     | 44ms (98.46%) |
| Ans 2 (Python) |                               |            |               |
| Ans 3 (Python) |                               |            |               |

解法一：

```python
class Leaderboard:

    def __init__(self):
        self.hashmap = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hashmap:
            self.hashmap[playerId] = score
        else:
            self.hashmap[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.hashmap.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        del self.hashmap[playerId]
```