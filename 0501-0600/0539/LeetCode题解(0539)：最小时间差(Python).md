# LeetCode题解(0539)：计算字符串表示时间列表中的最小时间差(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-time-difference/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 92ms (59.70%) |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 68ms (98.48%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 生成用分钟表示的时间
        lst = []
        for time in timePoints:
            hour, minute = time.split(":")
            lst.append(int(hour) * 60 + int(minute))

        # 排序时间列表
        lst.sort()

        # 计算最小时间差
        ans = lst[0] + 1440 - lst[-1]  # 首尾相差一天的最小值
        for i in range(len(lst) - 1):
            ans = min(ans, lst[i + 1] - lst[i])
        return ans
```

解法二（优化解法一）：

> 不再使用“:”分隔小时、分钟而直接使用切片器分隔
>
> 使用集合直接处理重复值

```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 生成用分钟表示的时间
        lst = set()
        for time in timePoints:
            minute = int(time[:2]) * 60 + int(time[3:])
            if minute in lst:
                return 0
            lst.add(minute)

        # 排序时间列表
        lst = sorted(lst)

        # 考虑跨午夜的情况
        lst.append(lst[0] + 1440)

        # 计算最小时间差
        return min(lst[i + 1] - lst[i] for i in range(len(lst) - 1))
```