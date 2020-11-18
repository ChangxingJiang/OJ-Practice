# LeetCode题解(Offer56II)：数组中数字出现的次数 II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/)（中等）

标签：位运算、数组、集合

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 64ms (79.14%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 96ms (45.91%) |
| Ans 3 (Python) |            |            |               |

解法一（集合）：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s1 = set()
        s2 = set()
        for n in nums:
            if n not in s2:
                if n in s1:
                    s1.remove(n)
                    s2.add(n)
                else:
                    s1.add(n)

        return s1.pop()
```

解法二（二进制位的状态转移）：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0  # 每个数的状态的二进制的个位
        two = 0  # 每个数的状态的二进制的十位
        for n in nums:
            one = one ^ n & ~two
            two = two ^ n & ~one
        return one
```