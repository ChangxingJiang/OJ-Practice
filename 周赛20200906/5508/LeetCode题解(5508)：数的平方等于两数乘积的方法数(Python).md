# LeetCode题解(5508)：数的平方等于两数乘积的方法数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)（中等）

标签：哈希表、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时         |
| -------------- | ---------- | ---------- | ---------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 2168ms (100.00%) |
| Ans 2 (Python) |            |            |                  |
| Ans 3 (Python) |            |            |                  |

解法一：

![LeetCode题解(5508)：截图](LeetCode题解(5508)：截图.png)

```python
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # 类型1
        ans = 0
        for i in range(len(nums1)):
            n1 = nums1[i] ** 2
            tmp = collections.Counter()
            for n2 in nums2:
                n3 = n1 / n2
                if n3 in tmp:
                    ans += tmp[n3]
                tmp[n2] += 1

        # 类型2
        for i in range(len(nums2)):
            n1 = nums2[i] ** 2
            tmp = collections.Counter()
            for n2 in nums1:
                n3 = n1 / n2
                if n3 in tmp:
                    ans += tmp[n3]
                tmp[n2] += 1

        return ans
```