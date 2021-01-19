# LeetCode题解(0915)：分割数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 212ms (75.44%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        lst1 = []
        lst2 = []
        for n in A:
            if not lst1 or lst1[-1] < n:
                lst1.append(n)
            else:
                lst1.append(lst1[-1])
        for n in A[::-1]:
            if not lst2 or lst2[-1] > n:
                lst2.append(n)
            else:
                lst2.append(lst2[-1])
        lst2.reverse()

        for i in range(len(A) - 1):
            if lst1[i] <= lst2[i + 1]:
                return i + 1
```

