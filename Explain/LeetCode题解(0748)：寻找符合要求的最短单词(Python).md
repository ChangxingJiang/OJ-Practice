# LeetCode题解(0748)：寻找符合要求的最短单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-completing-word/（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 76ms (95.30%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```
def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    patterns = list(filter(str.isalpha, licensePlate.lower()))
    ans = " " * 15
    for word in words:
        alpha = list(word)
        for p in patterns:
            if p not in alpha:
                break
            alpha.remove(p)
        else:
            if len(word) < len(ans):
                ans = word
    return ans
```