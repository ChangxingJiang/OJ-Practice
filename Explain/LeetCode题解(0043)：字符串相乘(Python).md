# LeetCode题解(0043)：字符串大数相乘(Python)

题目：[原题链接](https://leetcode-cn.com/problems/multiply-strings/)（中等）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M+N)$   | $O(1)$     | 144ms (55.52%) |
| Ans 2 (Python) | --         | --         | 32ms (99.35%)  |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def multiply(self, num1: str, num2: str) -> str:
    # 处理特殊情况
    if num1 == "0" or num2 == "0":
        return "0"

    N1 = len(num1)
    N2 = len(num2)
    N = N1 + N2

    ans = []
    step = 2
    now = 0
    while step <= N:
        for i1 in range(max(step - N2, 1), min(step, N1 + 1)):
            i2 = step - i1
            now += int(num1[-i1]) * int(num2[-i2])
        ans.append(str(now % 10))
        now //= 10
        step += 1
    while now:
        ans.append(str(now % 10))
        now //= 10

    return "".join(ans[::-1])
```

解法二（不符合题意的捣蛋解法）：

![LeetCode题解(0043)：截图1](LeetCode题解(0043)：截图1.png)

```python
def multiply(self, num1: str, num2: str) -> str:
    return str(int(num1) * int(num2))
```