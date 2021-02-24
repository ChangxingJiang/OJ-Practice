# LeetCode题解(1310)：子数组异或查询(Python)

题目：[原题链接](https://leetcode-cn.com/problems/xor-queries-of-a-subarray/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 516ms (10.17%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        now = 0
        for num in arr:
            now ^= num
            xor.append(now)

        ans = []
        for l, r in queries:
            ans.append(xor[r + 1] ^ xor[l])
        return ans
```

