# LeetCode题解(0459)：判断字符串中是否有重复的子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/repeated-substring-pattern/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n^2)     | O(1)       | 72ms (50.99%)  |
| Ans 2 (Python) | O(n)       | O(1)       | 40ms (92.28%)  |
| Ans 3 (Python) | O(n)       | O(n)       | 256ms (13.03%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    size = len(s)
    for i in range(1, size):
        # 若不是子串长度的整倍数则一定不是该长度子串的多次构成
        if size % i != 0:
            continue

        # 比较各部分子串是否相同
        differ = False
        pattern = s[:i]
        for j in range(1, size // i):
            sample = s[j * i:(j + 1) * i]
            if pattern != sample:
                differ = True
                break
        if not differ:
            return True
    else:
        return False
```

解法二（解法一的优化）：

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    size = len(s)
    for i in range(1, size // 2 + 1):
        # 若不是子串长度的整倍数则一定不是该长度子串的多次构成
        if size % i != 0:
            continue
        # 比较各部分子串是否相同
        if (s[:i] * (size // i)) == s:
            return True
    else:
        return False
```

解法三（KMP）：

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    size = len(s)
    next = [-1] * size
    for i in range(1, size):
        j = next[i - 1]
        while j >= 0 and s[j + 1] != s[i]:
            j = next[j]
        if s[j + 1] == s[i]:
            next[i] = j + 1
        print(next)
    return next[-1] >= 0 and size % (size - 1 - next[-1]) == 0
```