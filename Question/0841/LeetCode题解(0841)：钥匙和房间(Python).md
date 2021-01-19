# LeetCode题解(0841)：钥匙和房间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/keys-and-rooms/)（中等）

标签：图、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 76ms (77.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        queue = collections.deque([0])
        while queue:
            n1 = queue.popleft()
            for n2 in rooms[n1]:
                if n2 not in visited:
                    visited.add(n2)
                    queue.append(n2)
        return len(visited) == len(rooms)
```

