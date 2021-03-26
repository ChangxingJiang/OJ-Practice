# LeetCode题解(0421)：数组中两个数的最大异或值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/)（中等）

标签：位运算、字典树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogM)$ | $O(1)$     | 200ms (88.51%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = max(nums).bit_length()
        max_xor = 0
        for i in range(length)[::-1]:
            # 将上一位的最大异或值左移位
            max_xor <<= 1

            # 当前位目标最大异或值
            curr_xor = max_xor | 1

            # 计算每个数值当前长度的前缀
            prefixes = {num >> i for num in nums}

            # 如果确实找到了可以实现当前位目标最大异或值的值
            if any(curr_xor ^ p in prefixes for p in prefixes):
                max_xor |= 1

        return max_xor
```

