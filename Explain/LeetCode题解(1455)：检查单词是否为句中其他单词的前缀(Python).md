# LeetCode题解(1455)：检查单词是否为句中其他单词的前缀(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)（简单）

| 解法           | 时间复杂度                 | 空间复杂度 | 执行用时      |
| -------------- | -------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$ : N为句子中的单词数 | $O(N)$     | 36ms (84.27%) |
| Ans 2 (Python) |                            |            |               |
| Ans 3 (Python) |                            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    size = len(searchWord)
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        word = sentence[i]
        if size <= len(word):
            if searchWord == word[:size]:
                return i + 1
    else:
        return -1
```