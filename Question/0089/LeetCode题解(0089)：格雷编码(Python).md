# LeetCode题解(0089)：格雷编码(Python)

题目：[原题链接](https://leetcode-cn.com/problems/gray-code/)（中等）

标签：回溯算法、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 84ms (6.68%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []

        gray = 0
        while len(ans) < 2 ** n:
            ans.append(gray)
            gray ^= 1
            ans.append(gray)
            gray ^= (gray & -gray) << 1

        return ans
```

