# LeetCode题解(1535)：找出数组游戏的赢家(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-winner-of-an-array-game/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (77%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一（情景模拟）：

```python
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        size = len(arr)

        # 处理长度超过总长的情况
        if k >= size:
            return max(arr)

        now = arr[0]
        win = 0
        idx = 1

        while win < k:
            if arr[idx] > now:
                now = arr[idx]
                win = 1
            else:
                win += 1

            idx = (idx + 1) % size

        return now
```