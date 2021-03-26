# LeetCode题解(1550)：数组中存在连续三个奇数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/three-consecutive-odds/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (20%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        num = 0
        for n in arr:
            if n % 2 == 1:
                num += 1
                if num == 3:
                    return True
            else:
                num = 0
        return False
```