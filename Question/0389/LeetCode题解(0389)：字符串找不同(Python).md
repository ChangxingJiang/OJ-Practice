# LeetCode题解(0389)：字符串找不同(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-difference/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 40ms (87.66%) |
| Ans 2 (Python) | --         | --         | 44ms (71.54%) |
| Ans 2 (Python) | --         | --         | 40ms (87.66%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findTheDifference(self, s: str, t: str) -> str:
    for ch in t:
        if ch not in s:
            return ch
        else:
            s = s.replace(ch, "", 1)
```

解法二：

```python
def findTheDifference(self, s: str, t: str) -> str:
    count = collections.Counter(s)
    for c in t:
        if c not in count or count[c] == 0:
            return c
        else:
            count[c] -= 1
```

解法三（Pythonic）：

```python
def findTheDifference(self, s: str, t: str) -> str:
    return list((collections.Counter(t)-collections.Counter(s)).keys())[0]
```