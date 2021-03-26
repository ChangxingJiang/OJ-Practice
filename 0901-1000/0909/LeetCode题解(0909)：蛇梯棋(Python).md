# LeetCode题解(0909)：蛇梯棋(Python)

题目：[原题链接](https://leetcode-cn.com/problems/snakes-and-ladders/)（中等）

标签：广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 108ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])

        # 将蛇形棋转换为列表
        lst = [0]
        reverse = False
        for i in range(m - 1, -1, -1):
            if not reverse:
                lst.extend(board[i])
            else:
                lst.extend(reversed(board[i]))
            reverse = not reverse

        # 广度优先搜索
        step = 0
        visited = {1: 0}
        queue = collections.deque([1])
        while queue:
            step += 1
            for _ in range(len(queue)):
                n1 = queue.popleft()
                for n2 in range(n1 + 1, n1 + 7):
                    if n2 == m * n:
                        return step
                    if lst[n2] != -1:
                        n2 = lst[n2]
                    if n2 == m * n:
                        return step
                    if n2 not in visited or visited[n2] > step:
                        visited[n2] = step
                        queue.append(n2)

        return -1
```

