# LeetCode题解(1150)：检查一个数是否在数组中占绝大多数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)（简单）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (34.91%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 40ms (53.77%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        num = 0
        for n in nums:
            if n != target:
                num -= 1
            else:
                num += 1

        return num > 0
```

解法二（二分查找）：

```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        i1 = bisect.bisect_left(nums, target)  # 目标值的第1个数
        i2 = bisect.bisect_right(nums, target)  # 比目标值大的第1个数
        return i2 - i1 > len(nums) / 2
```