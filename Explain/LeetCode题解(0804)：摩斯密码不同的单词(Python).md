# LeetCode题解(0804)：摩斯密码不同的单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-morse-code-words/)（简单）

| 解法           | 时间复杂度                 | 空间复杂度 | 执行用时      |
| -------------- | -------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×k)$ : k为单词平均长度 | $O(N)$     | 44ms (78.68%) |
| Ans 2 (Python) | $O(N×k)$ : k为单词平均长度 | $O(N)$     | 44ms (78.68%) |
| Ans 3 (Python) |                            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    codes = set()
    for word in words:
        code = ""
        for c in word.lower():
            code += morse[ord(c) - 97]
        codes.add(code)

    return len(codes)
```

解法二（暴力解法的又一种形式）：

```python
def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    codes = set()
    for word in words:
        codes.add("".join([morse[ord(c) - 97] for c in word.lower()]))
    return len(codes)
```