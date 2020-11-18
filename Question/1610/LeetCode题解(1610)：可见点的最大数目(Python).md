# LeetCode题解(1610)：指定视角范围下平面内可见点的最大数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-visible-points/)（困难）

标签：数学、几何、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(P)$     | $O(P)$     | 852ms (28%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        another = 0

        # 计算所有角度
        angles = []
        for point in points:
            # 重叠的情况
            if point[0] == location[0] and point[1] == location[1]:
                another += 1

            # 垂直的情况
            elif point[0] == location[0]:
                if point[1] > location[1]:
                    angles.append(90)
                else:
                    angles.append(270)
            elif point[1] == location[1]:
                if point[0] > location[0]:
                    angles.append(0)
                else:
                    angles.append(180)

            # 处理其他角度的情况
            else:
                angles.append(math.degrees(math.atan2(point[1] - location[1], point[0] - location[0])))

        angles.sort()

        # 双指针最大值
        ans = 1
        left = 0
        right = 0
        while right - left < len(angles) and left < len(angles):
            if (angles[(right + 1) % len(angles)] - angles[left]) % 360 <= angle:
                right += 1
                ans = max(ans, min(right - left + 1, len(angles)))
            else:
                left += 1
        return ans + another
```