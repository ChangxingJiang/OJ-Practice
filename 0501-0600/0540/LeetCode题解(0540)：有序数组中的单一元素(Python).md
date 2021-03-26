# LeetCode题解(0540)：有序数组中的单一元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)（中等）

标签：二分查找、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (18.94%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 32ms (95.20%) |
| Ans 3 (Python) |            |            |               |

解法一（位运算）：

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
```

解法二（二分查找）：

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # 处理中间为偶数的情况（数组一共一定为奇数个元素）
            if m % 2 == 0:
                if nums[m] == nums[m + 1]:
                    l = m + 1
                else:
                    r = m

            # 处理中间为奇数的情况
            else:
                if nums[m] == nums[m - 1]:
                    l = m + 1
                else:
                    r = m

        return nums[l]
```

