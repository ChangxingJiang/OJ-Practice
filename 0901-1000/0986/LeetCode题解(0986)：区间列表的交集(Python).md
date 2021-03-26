# LeetCode题解(0986)：区间列表的交集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/interval-list-intersections/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(A+B)$   | $O(1)$     | 72ms (16.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i1, i2 = 0, 0
        while i1 < len(A) and i2 < len(B):
            left = max(A[i1][0], B[i2][0])
            right = min(A[i1][1], B[i2][1])
            if left <= right:
                ans.append([left, right])

            if A[i1][1] < B[i2][1]:
                i1 += 1
            else:
                i2 += 1

        return ans
```

