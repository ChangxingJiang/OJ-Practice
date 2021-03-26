# LeetCode题解(0338)：比特位计数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/counting-bits/)（中等）

标签：位运算、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 108ms (34.07%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i & (i - 1)] + 1)
        return ans
```

