# LeetCode题解(0345)：反转字符串中的元音字母(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/)（简单）

题目0344的延伸。

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 68ms (64.58%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针实现）：

```python
def reverseVowels(self, s: str) -> str:
    s = list(s)
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    i = 0
    j = len(s) - 1
    while i < j:
        while s[i] not in vowels and i < j:
            i += 1
        while s[j] not in vowels and i < j:
            j -= 1
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)
```

