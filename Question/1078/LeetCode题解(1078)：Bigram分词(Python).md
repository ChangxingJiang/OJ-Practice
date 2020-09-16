# LeetCode题解(1078)：Bigram分词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/occurrences-after-bigram/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (60.29%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    text = text.split(" ")
    ans = []
    for i in range(len(text) - 2):
        if text[i] == first and text[i + 1] == second:
            ans.append(text[i + 2])
    return ans
```