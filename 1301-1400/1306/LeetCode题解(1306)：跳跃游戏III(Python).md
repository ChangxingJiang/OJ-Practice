# LeetCode题解(1306)：跳跃游戏III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/jump-game-iii/)（中等）

标签：广度优先搜索、深度优先搜索、递归、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (88.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)

        dp = [False] * size
        dp[start] = True

        queue = collections.deque([start])

        while queue:
            now_idx = queue.popleft()

            # 已经找到结果
            if arr[now_idx] == 0:
                return True

            next_lst = [now_idx - arr[now_idx], now_idx + arr[now_idx]]
            for next_idx in next_lst:
                if 0 <= next_idx < size and not dp[next_idx]:
                    dp[next_idx] = True
                    queue.append(next_idx)

        return False
```