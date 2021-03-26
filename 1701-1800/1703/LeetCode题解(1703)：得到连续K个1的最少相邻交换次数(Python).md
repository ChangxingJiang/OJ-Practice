# LeetCode题解(1703)：得到连续K个1的最少相邻交换次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/)（困难）

标签：滑动窗口、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 272ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # 统计各个1之间的距离
        lst1 = []
        now = -1
        for num in nums:
            if num == 1:
                if now != -1:
                    lst1.append(now)
                now = 0
            else:
                if now != -1:
                    now += 1

        # 处理k==2的特殊情况
        if k == 2:
            return min(lst1)

        # 构造每一小段的列表
        # [1,2(2次),3(3次),4] = [1,2] + [2,3] + [3,4]
        size = k // 2
        times = (k + 1) // 2
        now = sum(lst1[:size])
        lst2 = [now]
        for i in range(len(lst1) - size):
            now = now - lst1[i] + lst1[i + size]
            lst2.append(now)

        # 滑动窗口
        ans = now = sum(lst2[:times])
        for i in range(len(lst2) - times):
            now = now - lst2[i] + lst2[i + times]
            ans = min(ans, now)

        return ans
```

