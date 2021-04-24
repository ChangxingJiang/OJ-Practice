# LeetCode题解(LCP30)：魔塔游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/p0NxJO/)（中等）

标签：堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 144ms (70.44%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
import heapq


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        room = []  # 当前扣血房间
        now = 1  # 当前血量

        if sum(nums) < 0:
            return -1

        ans = 0

        for num in nums:
            if num >= 0:  # 加血房间或不影响血量的房间
                now += num
            else:  # 扣血房间
                now += num
                heapq.heappush(room, num)
                while now <= 0 and room:  # 如果当前血量不是正值，则需要将之前扣血最多的房间移动到末尾（贪心）
                    now -= heapq.heappop(room)
                    ans += 1
                if now <= 0 and not room:  # 如果当前血量不是正值，且已经没有可以移动的房间，则说明无法通过
                    return -1

        return ans
```

