# LeetCode题解(1552)：将多个球放入指定位置的多个篮子后两球之间最小距离的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/magnetic-force-between-two-balls/)（中等）

标签：二分查找、排序、数组

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时        |
| -------------- | ------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(Nlog(NS))$ | $O(N)$     | 1112ms (49.40%) |
| Ans 2 (Python) |               |            |                 |
| Ans 3 (Python) |               |            |                 |

解法一：

```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 处理特殊情况
        if m == 2:
            return max(position) - min(position)

        position.sort()

        # 计算距离列表
        distances = []
        for i in range(len(position) - 1):
            distances.append(position[i + 1] - position[i])

        # print(distances)

        # 检查指定值能否成功
        def check(v):
            find = 0
            now = 0
            for d in distances:
                now += d
                if now >= v:
                    find += 1
                    now = 0
                if find >= m - 1:
                    return True
            return False

        # 二分查找结果
        left = 0
        right = position[-1] - position[0]

        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
```