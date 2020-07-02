# LeetCode题解(0953)：验证外星语词典的顺序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/verifying-an-alien-dictionary/)（简单）

| 解法           | 时间复杂度             | 空间复杂度 | 执行用时      |
| -------------- | ---------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×K)$ : K为单词长度 | $O(1)$     | 36ms (95.67%) |
| Ans 2 (Python) | $O(N×K)$ : K为单词长度 | $O(1)$     | 44ms (72.67%) |
| Ans 3 (Python) |                        |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def isAlienSorted(self, words: List[str], order: str) -> bool:
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        for (c1, c2) in zip(word1, word2):
            if order.index(c1) < order.index(c2):
                break
            elif order.index(c1) > order.index(c2):
                return False
        else:
            if len(word1) > len(word2):
                return False
    return True
```

解法二（先制作查询词典）：

```python
def isAlienSorted(self, words: List[str], order: str) -> bool:
    dictionary = [-1] * 26
    for i in range(len(order)):
        dictionary[ord(order[i]) - 97] = i

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        for (c1, c2) in zip(word1, word2):
            o1 = dictionary[ord(c1) - 97]
            o2 = dictionary[ord(c2) - 97]
            if o1 < o2:
                break
            elif o1 > o2:
                return False
        else:
            if len(word1) > len(word2):
                return False
    return True
```