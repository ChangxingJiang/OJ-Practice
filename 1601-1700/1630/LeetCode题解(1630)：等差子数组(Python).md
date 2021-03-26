# LeetCode题解(1630)：判断是否可以重排为等差子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/arithmetic-subarrays/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 84ms (100%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_equal(ll):
            ll.sort()

            if len(ll) <= 2:
                return True

            d = ll[1] - ll[0]
            for j in range(2, len(ll)):
                if ll[j] - ll[j - 1] != d:
                    return False

            return True

        m = len(l)

        ans = []

        for i in range(m):
            left = l[i]
            right = r[i]

            lst = nums[left:right + 1]
            ans.append(is_equal(lst))

        return ans
```