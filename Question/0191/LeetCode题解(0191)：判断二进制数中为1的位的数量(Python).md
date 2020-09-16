# LeetCode题解(0191)：判断二进制数中为1的位的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-1-bits/)（简单）

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 28ms (>99.12%) |
| Ans 2 (Python) | 44ms (>52.18%) |

解法一（转换为字符串统计）：

```python
def hammingWeight(self, n: int) -> int:
    ans = 0
    for s in "{:032b}".format(n):
        if s == "1":
            ans += 1
    return ans
```

解法二（位运算）：

```python
def hammingWeight(self, n: int) -> int:
    ans = 0
    for i in range(32):
        if n & 1 == 1:
            ans += 1
        n >>= 1
    return ans
```