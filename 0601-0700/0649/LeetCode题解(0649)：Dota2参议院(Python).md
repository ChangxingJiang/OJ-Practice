# LeetCode题解(0649)：Dota2参议院(Python)

题目：[原题链接](https://leetcode-cn.com/problems/dota2-senate/)（中等）

标签：贪心算法、队列

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 60ms (94.51%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        size = len(senate)

        queue1 = collections.deque()
        queue2 = collections.deque()
        for i, ch in enumerate(senate):
            if ch == "R":
                queue1.append(i)
            else:
                queue2.append(i)

        while queue1 and queue2:
            if queue1[0] < queue2[0]:
                queue1.append(queue1.popleft() + size)
                queue2.popleft()
            else:
                queue2.append(queue2.popleft() + size)
                queue1.popleft()

        return "Radiant" if queue1 else "Dire"
```