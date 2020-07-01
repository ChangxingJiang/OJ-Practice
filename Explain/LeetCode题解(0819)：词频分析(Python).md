# LeetCode题解(0819)：词频分析(Python)

题目：[原题链接](https://leetcode-cn.com/problems/most-common-word/)（简单）

| 解法           | 时间复杂度                              | 空间复杂度 | 执行用时      |
| -------------- | --------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+B)$ : N为句子长度、B为禁用列表长度 | $O(N+B)$   | 40ms (92.22%) |
| Ans 2 (Python) |                                         |            |               |
| Ans 3 (Python) |                                         |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    hashmap = {}
    for word in re.split("[ ,.?!]", paragraph.lower()):
        word = "".join(list(filter(str.isalpha, word)))
        if len(word) > 0:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] += 1

    times = 0
    ans = ""
    for key, value in hashmap.items():
        if value > times and key not in banned:
            ans = key
            times = value
    return ans
```