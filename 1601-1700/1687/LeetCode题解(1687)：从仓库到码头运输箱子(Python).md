# LeetCode题解(1687)：从仓库到码头运输箱子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delivering-boxes-from-storage-to-ports/)（困难）

标签：动态规划、滑动窗口、线段树、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 460ms (95.19%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)

        dp = [0] * n  # dp[i]表示到i个箱子的最小路径
        ans = 0  # 持续维护为当前窗口的路程总和

        left = -1  # left=窗口左侧边界
        for right in range(n):  # right=窗口右侧边界
            maxBoxes -= 1
            maxWeight -= boxes[right][1]

            # 从仓库出发的一趟新旅程（增加来回两趟）
            if right == left + 1:
                ans += 2

            # 和上一个箱子不是同一个目标（增加从港口到港口的一趟）
            elif boxes[right][0] != boxes[right - 1][0]:
                ans += 1

            # 移动窗口的左侧边缘（如果dp[left]==dp[left+1]，那么说明窗口左侧边缘可以无损地向右移动，直接向右移动即可）
            while maxBoxes < 0 or maxWeight < 0 or (left < right - 1 and dp[left] == dp[left + 1]):
                left += 1
                maxBoxes += 1
                maxWeight += boxes[left][-1]
                if boxes[left][0] != boxes[left + 1][0]:
                    ans -= 1

            dp[right] = dp[left] + ans

        return dp[-1]
```

