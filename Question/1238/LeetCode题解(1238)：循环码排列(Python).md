# LeetCode题解(1238)：循环码排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/circular-permutation-in-binary-representation/)（中等）

标签：数学、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(1)$     | 204ms (48.94%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = []
        for i in range(1 << n):
            ans.append(i ^ (i >> 1) ^ start)  # 新各类编码为标准各类编码异或start
        return ans
```

