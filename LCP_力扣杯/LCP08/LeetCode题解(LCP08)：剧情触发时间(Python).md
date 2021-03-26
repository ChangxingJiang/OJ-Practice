# LeetCode题解(LCP08)：剧情触发时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ju-qing-hong-fa-shi-jian/)（中等）

标签：二分查找

| 解法           | 时间复杂度                                          | 空间复杂度 | 执行用时       |
| -------------- | --------------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×logM)$ : n=len(requirements) ; m=len(increase) | $O(M)$     | 392ms (95.31%) |
| Ans 2 (Python) |                                                     |            |                |
| Ans 3 (Python) |                                                     |            |                |

解法一：

```python
class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        C = [0]
        R = [0]
        H = [0]
        for c, r, h in increase:
            C.append(C[-1] + c)
            R.append(R[-1] + r)
            H.append(H[-1] + h)

        ans = []
        for c, r, h in requirements:
            d1 = bisect.bisect_left(C, c)
            d2 = bisect.bisect_left(R, r)
            d3 = bisect.bisect_left(H, h)
            d = max(d1, d2, d3)
            ans.append(d if d <= len(increase) else -1)

        return ans
```

