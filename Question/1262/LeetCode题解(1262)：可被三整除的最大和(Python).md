# LeetCode题解(1262)：可被三整除的最大和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/)（中等）

标签：数学、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 84ms (83.69%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = 0
        n1, n2 = [], []

        for num in nums:
            mod = num % 3
            if mod == 0:
                ans += num
            elif mod == 1:
                n1.append(num)
            else:
                n2.append(num)

        n1.sort()
        n2.sort()

        if len(n1) < len(n2):
            n1, n2 = n2, n1

        if (len(n1) - len(n2)) % 3 == 2:
            return ans + max(sum(n1[2:]) + sum(n2),
                             (sum(n1) + sum(n2[1:])) if len(n1) >= 3 and len(n2) >= 1 else 0)
        elif (len(n1) - len(n2)) % 3 == 1:
            return ans + max(sum(n1[1:]) + sum(n2),
                             (sum(n1) + sum(n2[2:])) if len(n1) >= 3 and len(n2) >= 2 else 0)
        else:
            return ans + sum(n1) + sum(n2)
```

