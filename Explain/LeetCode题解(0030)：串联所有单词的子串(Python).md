# LeetCode题解(0030)：匹配字符串中由指定列表串联形成的所有子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)（困难）

标签：字符串、哈希表、双指针、滑动窗口

| 解法           | 时间复杂度                                          | 空间复杂度 | 执行用时       |
| -------------- | --------------------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M×L^2)$ : 其中M为words中词数，L为words中词长度 | $O(M×L)$   | 704ms (61.09%) |
| Ans 2 (Python) | $O(N×L)$ : L为words中词长度                         | $O(M×L)$   | 112ms (81.47%) |
| Ans 3 (Python) |                                                     |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def findSubstring(self, s: str, words: List[str]) -> List[int]:
    # 处理特殊情况
    if not s or not words:
        return []

    L = len(words[0])
    total = len(words[0]) * len(words)
    words = collections.Counter(words)
    N = len(s)
    ans = []
    for i in range(N - total + 1):
        tmp = [s[i + j:i + j + L] for j in range(0, total, L)]
        for key, value in words.items():
            if tmp.count(key) != value:
                break
        else:
            ans.append(i)
    return ans
```

解法二（移动窗口）：

```python
def findSubstring(self, s: str, words: List[str]) -> List[int]:
    # 处理特殊情况
    if not s or not words:
        return []

    L = len(words[0])
    total = L * len(words)
    words = collections.Counter(words)
    N = len(s)
    ans = []
    for i in range(L):
        left = i
        right = i
        now = collections.Counter()
        while right < N:
            if right - left < total:
                now[s[right:right + L]] += 1
                right += L
                if right - left == total and now == words:
                    ans.append(left)
            elif right - left == total:
                now[s[left:left + L]] -= 1
                if now[s[left:left + L]] == 0:
                    del now[s[left:left + L]]
                now[s[right:right + L]] += 1
                left += L
                right += L
                if now == words:
                    ans.append(left)
    return ans
```

