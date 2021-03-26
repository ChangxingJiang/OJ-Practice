# LeetCode题解(0881)：救生艇(Python)

题目：[原题链接](https://leetcode-cn.com/problems/boats-to-save-people/)（中等）

标签：贪心算法、双指针、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 108ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ans = 0

        i1, i2 = 0, len(people) - 1
        while i1 <= i2:
            while i1 < i2 and people[i1] + people[i2] > limit:
                i2 -= 1
                ans += 1
            i1 += 1
            i2 -= 1
            ans += 1

        return ans
```

