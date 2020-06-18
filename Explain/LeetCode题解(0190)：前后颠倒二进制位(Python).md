# LeetCode题解(0190)：前后颠倒二进制位(Python)

[题目链接](https://leetcode-cn.com/problems/reverse-bits/)（简单）

解法一（转换为字符串倒序）：

```python
def reverseBits(self, n: int) -> int:
    return int("0b" + "{:032b}".format(n)[::-1], 2)
```

解法二（位运算）：

```python
def reverseBits(self, n: int) -> int:
    res = 0
    for i in range(32):
        res <<= 1  # 将res左移一位
        res += n & 1  # 使用或运算，判断n的最右一位是否为1，如果为1则填到res的最右一位中
        n >>= 1  # 将n右移一位
    return res
```

