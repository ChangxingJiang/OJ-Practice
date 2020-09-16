# LeetCode题解(0500)：判断单词是否可以在键盘的同一行中打出来(Python)

题目：[原题链接](https://leetcode-cn.com/problems/keyboard-row/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 40ms (68.23%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findWords(self, words: List[str]) -> List[str]:
    keyboard = {
        "Q": 0, "W": 0, "E": 0, "R": 0, "T": 0, "Y": 0, "U": 0, "I": 0, "O": 0, "P": 0,
        "A": 1, "S": 1, "D": 1, "F": 1, "G": 1, "H": 1, "J": 1, "K": 1, "L": 1,
        "Z": 2, "X": 2, "C": 2, "V": 2, "B": 2, "N": 2, "M": 2
    }

    def helper(word):
        return len(set([keyboard[s] for s in word.upper()])) == 1

    return [word for word in words if helper(word)]
```