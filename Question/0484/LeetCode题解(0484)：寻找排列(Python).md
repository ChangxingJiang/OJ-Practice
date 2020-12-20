# LeetCode题解(0484)：寻找排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-permutation/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 100ms (59.57%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        lst = [[0]]
        for ch in s:
            if ch == "I":
                lst.append([0])
            else:
                lst[-1].append(lst[-1][-1] - 1)

        ans = []
        max_val = 0
        for part in lst:
            min_val = part[-1] - 1
            for n in part:
                ans.append(max_val + n - min_val)
            max_val -= min_val

        return ans
```