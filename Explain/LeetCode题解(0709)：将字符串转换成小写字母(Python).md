# LeetCode题解(0709)：将字符串转换成小写字母(Python)

题目：[原题链接](https://leetcode-cn.com/problems/to-lower-case/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 36ms (84.28%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 40ms (63.45%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def toLowerCase(self, str: str) -> str:
    return str.lower()
```

解法二：

```python
def toLowerCase(self, str: str) -> str:
    ans = ""
    for n in str:
        a = ord(n)
        if 65 <= ord(n) <= 90:
            ans += chr(a + 32)
        else:
            ans += n
    return ans
```