# LeetCode题解(Offer53I)：计算排序数组中指定数字的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)（简单）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (60.00%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 44ms (60.00%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count1(target)
```

解法二：

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)
```