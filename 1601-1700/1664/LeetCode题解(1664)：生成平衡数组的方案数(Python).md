# LeetCode题解(1664)：生成平衡数组的方案数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ways-to-make-a-fair-array/)（中等）

标签：贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 392ms (65.59%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        t1, t2 = 0, 0
        for i, n in enumerate(nums):
            if i % 2 == 1:
                t1 += n
            else:
                t2 += n

        # print("奇数和:", t1, "偶数和:", t2)

        ans = 0

        n1, n2 = 0, 0
        for i, n in enumerate(nums):
            s1 = t1 - n1
            s2 = t2 - n2
            if i % 2 == 1:
                s1 -= n
            else:
                s2 -= n

            if n1 + s2 == n2 + s1:
                ans += 1

            if i % 2 == 1:
                n1 += n
            else:
                n2 += n

        return ans
```

