# LeetCode题解(0718)：最长重复子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)（中等）

标签：二分查找、哈希表、数组、动态规划

| 解法           | 时间复杂度                      | 空间复杂度 | 执行用时     |
| -------------- | ------------------------------- | ---------- | ------------ |
| Ans 1 (Python) | $O((N1+N2)×N1×log(min(N1,N2)))$ | $O(N1^2)$  | 5964ms (28%) |
| Ans 2 (Python) |                                 |            |              |
| Ans 3 (Python) |                                 |            |              |

解法一（二分查找）：

```python
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(v):
            hashmap = set()
            for i in range(len(A) - v + 1):
                hashmap.add("".join(str(a) for a in A[i:i + v]))
            for i in range(len(B) - v + 1):
                if "".join(str(b) for b in B[i:i + v]) in hashmap:
                    return True
            return False

        ans = 0
        left, right = 0, min(len(A), len(B)) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans
```