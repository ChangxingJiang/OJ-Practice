# LeetCode题解(0504)：将整数转换为七进制(Python)

题目：[原题链接](https://leetcode-cn.com/problems/base-7/)（简单）

题目标签：

| 解法           | 执行用时      |
| -------------- | ------------- |
| Ans 1 (Python) | 40ms (70.46%) |
| Ans 2 (Python) | 40ms (70.46%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def convertToBase7(self, num: int) -> str:
    if num > 0:
        ans = ""
        while num > 0:
            ans += str(num % 7)
            num //= 7
        return ans[::-1]
    elif num == 0:
        return "0"
    else:
        num = abs(num)
        ans = ""
        while num > 0:
            ans += str(num % 7)
            num //= 7
        return "-" + ans[::-1]
```

解法二：

```python
def convertToBase7(self, num: int) -> str:
    minus = False
    if num < 0:
        minus = True
        num = -num

    ans = []
    while num >= 7:
        ans.append(str(num % 7))
        num //= 7
    ans.append(str(num))

    if minus:
        ans.append("-")

    ans.reverse()
    return "".join(ans)
```