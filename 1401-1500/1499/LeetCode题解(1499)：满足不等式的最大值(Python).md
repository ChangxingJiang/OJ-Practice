# LeetCode题解(1499)：满足不等式的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-value-of-equation/)（困难）

标签：数组、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 252ms (100%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = None

        # 每个元素最多被遍历两次，添加一次，删除一次
        # 队列内单调递减

        queue = collections.deque([])
        for x2, y2 in points:
            # 移除队列中已经超出窗口的点
            while queue:
                x1, y1 = queue[0]
                if x1 < x2 - k:
                    queue.popleft()
                else:
                    break

            # print(x2, "DEL", "->", queue)

            # 如果队列中存在元素，计算当前的结果
            if queue:
                x1, y1 = queue[0]
                if queue[0] != 0:
                    value = y1 + y2 + (x2 - x1)
                    if ans is None or ans < value:
                        ans = value

            # 将当前结果加入等待区，并移除等待区开头所有小于当前结果的值
            while queue:
                x1, y1 = queue[-1]
                if (x2 - x1) + y1 <= y2:
                    queue.pop()
                else:
                    break
            queue.append((x2, y2))

            # print(x2, "ADD", "->", queue)

        return ans
```