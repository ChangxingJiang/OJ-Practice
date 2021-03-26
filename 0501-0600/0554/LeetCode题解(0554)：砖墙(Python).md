# LeetCode题解(0554)：砖墙(Python)

题目：[原题链接](https://leetcode-cn.com/problems/brick-wall/)（中等）

标签：哈希表

| 解法           | 时间复杂度           | 空间复杂度 | 执行用时       |
| -------------- | -------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$ : N为砖块总数 | $O(N)$     | 204ms (94.75%) |
| Ans 2 (Python) |                      |            |                |
| Ans 3 (Python) |                      |            |                |

解法一：

```python
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total = len(wall)
        interval = collections.Counter()
        for w in wall:
            now = 0
            for n in w[:-1]:
                now += n
                interval[now] += 1

        ans = interval.most_common(1)
        return total - (ans[0][1] if ans else 0)
```