# LeetCode题解(1213)：三个有序数组的交集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/intersection-of-three-sorted-arrays/)（简单）

标签：哈希表、二分查找、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(1)$     | 116ms (37.02%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（二分查找）：

```python
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        s1, s2, s3 = len(arr1), len(arr2), len(arr3)

        ans = []

        i1, i2, i3 = 0, 0, 0
        while i1 < s1 and i2 < s2 and i3 < s3:
            if arr1[i1] == arr2[i2] == arr3[i3]:
                ans.append(arr1[i1])
                i1 += 1
            else:
                v = max(arr1[i1], arr2[i2], arr3[i3])
                i1 = bisect.bisect_left(arr1, v, lo=i1)
                i2 = bisect.bisect_left(arr2, v, lo=i2)
                i3 = bisect.bisect_left(arr3, v, lo=i3)

        return ans
```