# LeetCode题解(0804)：计算多个单词转换的摩斯密码数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-morse-code-words/)（简单）

标签：字符串

| 解法           | 时间复杂度                 | 空间复杂度 | 执行用时      |
| -------------- | -------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×k)$ : k为单词平均长度 | $O(N)$     | 44ms (78.68%) |
| Ans 2 (Python) | $O(N×k)$ : k为单词平均长度 | $O(N)$     | 36ms (95.83%) |
| Ans 3 (Python) |                            |            |               |

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