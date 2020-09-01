# LeetCode题解(1404)：依据指定规则将二进制表示减到1的步骤数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)（中等）

标签：字符串、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (84.66%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 44ms (65.03%) |
| Ans 3 (Python) |            |            |               |

解法一（情景模拟）：

```python
class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, base=2)
        ans = 0
        while num > 1:
            if num % 2 == 1:
                num += 1
                ans += 1
            else:
                num //= 2
                ans += 1
        return ans
```

解法二（归纳规律）：

```python
class Solution:
    def numSteps(self, s: str) -> int:
        has_one = False
        ans = 0
        for ch in s[1:][::-1]:
            if ch == "0":
                ans += 2 if has_one else 1
            else:
                ans += 1 if has_one else 2
                has_one = True
        return ans + 1 if has_one else ans
```