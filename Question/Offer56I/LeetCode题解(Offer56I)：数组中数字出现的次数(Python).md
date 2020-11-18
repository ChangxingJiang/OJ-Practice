# LeetCode题解(Offer56I)：寻找数组中仅出现一次的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)（中等）

标签：位运算、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 60ms (68.74%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 找到只出现了一次的两个数的异或结果
        lst = 0
        for n in nums:
            lst ^= n

        # 找到两个数第一个不相同的位
        diff = 1
        while diff & lst == 0:
            diff <<= 1

        # 依据第一个不相同的位对该位的两种情况分别进行异或操作（此时每组只有一个出现一次的数）
        a, b = 0, 0
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n

        return [a, b]
```