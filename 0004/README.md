# LeetCode题解：0004

[题目链接](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)（中等）

| 解法           | 时间复杂度         | 空间复杂度 | 执行用时       | 内存消耗        |
| -------------- | ------------------ | ---------- | -------------- | --------------- |
| Ans 1 (Python) | $O((M+N)log(M+N))$ | $O(M+N)$   | 40ms (>98.73%) | 13.7MB (>6.15%) |
| Ans 2 (Python) | $O(M+N)$           | $O(1)$     | 48ms (>89.95%) | 13.7MB (>6.15%) |
| Ans 3 (Python) | $O(log(M+N))$      | $O(1)$     | 80ms (>11.71%) | 13.8MB (>6.15%) |

解法一（直接合并数组排序求中位数）：

```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()
    count = len(nums)
    if count % 2 == 0:
        return (nums[int(count / 2 - 1)] + nums[int(count / 2)]) / 2
    else:
        return nums[int(count / 2)]
```

解法二（直接寻找中位数的位置）：

```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    len_1 = len(nums1)
    len_2 = len(nums2)
    total = len_1 + len_2

    left = -1
    right = -1

    index_1 = 0
    index_2 = 0

    for i in range(int(total / 2) + 1):
        left = right
        if index_1 < len_1 and (index_2 >= len_2 or nums1[index_1] < nums2[index_2]):
            right = nums1[index_1]
            index_1 += 1
        else:
            right = nums2[index_2]
            index_2 += 1

    if total % 2 == 0:
        return (left + right) / 2
    else:
        return right
```

解法三（使用二分查找寻找中位数的位置）：



