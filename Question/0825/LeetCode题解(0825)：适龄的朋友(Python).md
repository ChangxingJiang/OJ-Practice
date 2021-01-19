# LeetCode题解(0825)：适龄的朋友(Python)

题目：[原题链接](https://leetcode-cn.com/problems/friends-of-appropriate-ages/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(121^2+N)$ | $O(121)$   | 200ms (41.03%) |
| Ans 2 (Python) |              |            |                |
| Ans 3 (Python) |              |            |                |

解法一：

```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for age1, n1 in enumerate(count):
            for age2, n2 in enumerate(count):
                if age1 * 0.5 + 7 >= age2:
                    continue
                if age1 < age2:
                    continue
                if age1 < 100 < age2:
                    continue

                if age1 == age2:
                    ans += n1 * (n1 - 1)
                else:
                    ans += n1 * n2

        return ans
```

