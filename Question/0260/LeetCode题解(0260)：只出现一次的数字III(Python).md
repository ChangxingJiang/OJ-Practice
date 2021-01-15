# LeetCode题解(0260)：只出现一次的数字III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/single-number-iii/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (87.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 异或找到出现次数为奇数次的二进制位
        xor1 = 0
        for num in nums:
            xor1 ^= num

        # 找到第1个（从右往左）出现次数为奇数次的二进制位
        diff = xor1 & (-xor1)

        # 异或找到第1个出现次数为奇数次的二进制位为1的出现次数为奇数次的数（此时只会有1个）
        xor2 = 0
        for num in nums:
            if diff & num:
                xor2 ^= num

        return [xor1 ^ xor2, xor2]
```

