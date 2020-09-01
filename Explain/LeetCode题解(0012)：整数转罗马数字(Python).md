# LeetCode题解(0012)：将整数转换为罗马数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/integer-to-roman/)（中等）

标签：字符串、数学、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 60ms (72.76%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 56ms (85.08%) |
| Ans 3 (Python) | $O(1)$     | $O(1)$     | 68ms (39.91%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（硬编码数字法）：

```python
def intToRoman(self, num: int) -> str:
    def translate(n, sign1, sign2, sign3):
        if n == 0:
            return ""
        elif 1 <= n <= 3:
            return sign1 * n
        elif n == 4:
            return sign1 + sign2
        elif 5 <= n <= 8:
            return sign2 + sign1 * (n - 5)
        elif n == 9:
            return sign1 + sign3

    a = translate(num // 1000, "M", "", "")
    b = translate(num % 1000 // 100, "C", "D", "M")
    c = translate(num % 100 // 10, "X", "L", "C")
    d = translate(num % 10, "I", "V", "X")
    return a + b + c + d
```

解法二（更彻底的硬编码数字法）：

```python
def intToRoman(self, num: int) -> str:
    B4 = ["", "M", "MM", "MMM"]
    B3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    B2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    B1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return B4[num // 1000] + B3[num % 1000 // 100] + B2[num % 100 // 10] + B1[num % 10]
```

解法三（贪心算法）：

```python
def intToRoman(self, num: int) -> str:
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
             (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    ans = []
    for n, s in table:
        count, num = divmod(num, n)
        ans.append(count * s)

    return "".join(ans)
```