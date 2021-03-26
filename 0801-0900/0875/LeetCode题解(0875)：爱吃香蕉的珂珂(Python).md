# LeetCode题解(0875)：爱吃香蕉的珂珂(Python)

题目：[原题链接](https://leetcode-cn.com/problems/koko-eating-bananas/)（中等）

标签：二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogM)$ | $O(1)$     | 552ms (12.77%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, sum(piles)
        while left < right:
            mid = (left + right) // 2

            # 计算需要吃的时间
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time > H:
                left = mid + 1
            else:
                right = mid

        return left
```

