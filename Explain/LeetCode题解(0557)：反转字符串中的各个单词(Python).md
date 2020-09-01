# LeetCode题解(0557)：反转字符串中的各个单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (77.36%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 60ms (34.45%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 36ms (96.64%) |

解法一（字符串分隔）：

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split(" ")
        for i in range(len(n)):
            n[i] = n[i][::-1]
        return " ".join(n)
```

解法二（字符串遍历）：

```python
def reverseWords(self, s: str) -> str:
    last = 0
    ans = ""
    for i in range(len(s)):
        if s[i] == " ":
            ans += s[last:i][::-1] + " "
            last = i + 1
    else:
        ans += s[last:][::-1]
    return ans
```

解法三：

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split()
        ans = []
        for i in range(len(n)):
            ans.append(n[i][::-1])
        return " ".join(ans)
```