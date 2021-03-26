# LeetCode题解(0720)：词典中最长的单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-word-in-dictionary/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×K)$   | $O(N)$     | 212ms (21.70%) |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 84ms (97.17%)  |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def longestWord(self, words: List[str]) -> str:
    words.sort()

    last_list = []
    now_list = []
    for size in range(1, 31):
        for word in words:
            if len(word) == size and (size == 1 or word[:-1] in last_list):
                now_list.append(word)
        if len(now_list) == 0:
            break
        last_list = now_list
        now_list = []

    minimum = len(words)
    ans = None
    for word in last_list:
        idx = words.index(word)
        if idx < minimum:
            minimum = idx
            ans = word

    return ans
```

解法二（排序+哈希表）：

```python
def longestWord(self, words: List[str]) -> str:
    if len(words) == 0:
        return ""

    words.sort()

    maximum = 0
    ans = ""
    hashmap = set()
    for word in words:
        if len(word) == 1:
            hashmap.add(word)
        elif word[:-1] in hashmap:
            hashmap.add(word)
            if len(word) > maximum:
                maximum = len(word)
                ans = word
    return ans
```