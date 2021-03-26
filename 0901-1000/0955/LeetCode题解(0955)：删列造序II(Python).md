# LeetCode题解(0955)：删列造序II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-columns-to-make-sorted-ii/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M)$     | 48ms (86.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])

        ans = 0
        same_list = {i for i in range(m - 1)}
        for j in range(n):
            remove_list = set()
            for i in range(m - 1):
                if A[i][j] > A[i + 1][j] and i in same_list:
                    ans += 1
                    break
                elif A[i][j] < A[i + 1][j]:
                    if i in same_list:
                        remove_list.add(i)
            else:
                if not same_list:
                    return ans
                same_list -= remove_list

        return ans
```

