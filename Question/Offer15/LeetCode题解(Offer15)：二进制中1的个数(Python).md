# LeetCode题解(Offer15)：计算二进制数中1的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)（简单）

标签：位运算

| 解法           | 时间复杂度                 | 空间复杂度 | 执行用时      |
| -------------- | -------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$ : 其中N为二进制位数 | $O(1)$     | 44ms (53.95%) |
| Ans 2 (Python) |                            |            |               |
| Ans 3 (Python) |                            |            |               |

解法一：

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
```