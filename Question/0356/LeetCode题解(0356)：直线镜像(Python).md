# LeetCode题解(0356)：直线镜像(Python)

题目：[原题链接](https://leetcode-cn.com/problems/line-reflection/)（中等）

标签：几何、数学、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 48ms (98.11%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        count = collections.defaultdict(set)  # 以点(x,y)的y为key，x为值
        for x, y in points:
            count[y].add(x)

        val = None
        for x, lst in count.items():
            lst = list(sorted(lst))
            if len(lst) % 2 == 1:
                mid = lst[len(lst) // 2]
            else:
                mid = (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
            # 检查自身是否相对中线对称
            left, right = 0, len(lst) - 1
            while left < right:
                if lst[right] - mid != mid - lst[left]:
                    return False
                left += 1
                right -= 1
            # 检查中线是否一致
            if val is None:
                val = mid
            elif val != mid:
                return False

        return True
```