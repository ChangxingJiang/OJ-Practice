# LeetCode题解(Offer51)：计算数组中逆序对的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)（困难）

标签：数组、数学、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 2464ms (6.88%)  |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 1452ms (91.75%) |
| Ans 3 (Python) |            |            |                 |

解法一（二分查找）：

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        prefix = []
        for n in nums:
            left, right = 0, len(prefix)
            while left < right:
                mid = (left + right) // 2
                if n >= prefix[mid]:
                    left = mid + 1
                else:
                    right = mid
            ans += len(prefix) - left
            prefix.insert(left, n)
        return ans
```

解法二（解法一优化）：

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        prefix = []
        for n in nums:
            left, right = 0, len(prefix)
            while left < right:
                mid = (left + right) // 2
                if n >= prefix[mid]:
                    left = mid + 1
                else:
                    right = mid
            ans += len(prefix) - left
            prefix[left:left] = [n]
        return ans
```