# LeetCode题解(1710)：卡车上的最大单元数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-units-on-a-truck/)（简单）

标签：贪心算法、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 52ms (75.05%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        idx = 0
        while truckSize > 0 and idx < len(boxTypes):
            ans += boxTypes[idx][1] * min(boxTypes[idx][0], truckSize)
            truckSize -= boxTypes[idx][0]
            idx += 1

        return ans
```

