# LeetCode题解(LCP18)：早餐组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/2vYnGI/)（简单）

标签：滑动窗口、排序

| 解法           | 时间复杂度           | 空间复杂度 | 执行用时       |
| -------------- | -------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N1logN1+N2logN2)$ | $O(N1+N2)$ | 476ms (64.08%) |
| Ans 2 (Python) |                      |            |                |
| Ans 3 (Python) |                      |            |                |

解法一（滑动窗口）：

```python
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()

        s1, s2 = len(staple), len(drinks)

        i2 = 0
        while i2 < s2 and staple[0] + drinks[i2] <= x:
            i2 += 1

        ans = 0
        for i1 in range(s1):
            while i2 > 0 and staple[i1] + drinks[i2 - 1] > x:
                i2 -= 1
            ans += i2

        return ans % 1000000007
```