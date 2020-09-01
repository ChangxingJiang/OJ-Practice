# LeetCode题解(1451)：依据指定规则重新排列句子中的单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rearrange-words-in-a-sentence/)（中等）

标签：排序、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 52ms (79.32%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（自定义排序）：

```python
def arrangeWords(self, text: str) -> str:
    def helper(n):
        return len(n)

    ans = sorted(text.lower().split(" "), key=helper)
    ans[0] = ans[0].title()

    return " ".join(ans)
```