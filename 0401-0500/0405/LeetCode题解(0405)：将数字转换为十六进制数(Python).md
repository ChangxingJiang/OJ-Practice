# LeetCode题解(0405)：将数字转换为十六进制数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/)（简单）

| 解法           | 执行用时      |
| -------------- | ------------- |
| Ans 1 (Python) | 28ms (98.40%) |
| Ans 2 (Python) | 40ms (66.33%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（正负分别处理）：

```python
def toHex(self, num: int) -> str:
    if num >= 0:
        return str(hex(num))[2:]
    else:
        return str(hex(int("FFFFFFFF", base=16) + num + 1))[2:]
```

解法二：

```python
def toHex(self, num: int) -> str:
    if num < 0:
        num = (pow(2, 32) - 1) - abs(num) + 1
    elif num == 0:
        return "0"
    ans = []
    while num > 0:
        d = str(num % 16)
        if d == "10":
            d = "a"
        elif d == "11":
            d = "b"
        elif d == "12":
            d = "c"
        elif d == "13":
            d = "d"
        elif d == "14":
            d = "e"
        elif d == "15":
            d = "f"
        ans.append(d)
        num //= 16
    ans.reverse()
    return "".join(ans)
```