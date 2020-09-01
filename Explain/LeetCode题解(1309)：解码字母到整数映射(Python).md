# LeetCode题解(1309)：解码字母到整数映射(Python)

题目：[原题链接](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (96.97%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 44ms (55.89%) |
| Ans 3 (Python) |            |            |               |

解法一（双指针）：

```python
def freqAlphabets(self, s: str) -> str:
    ans = ""
    idx = 0
    for i in range(len(s)):
        if i - idx > 2:
            ans += chr(int(s[idx]) + 96)
            idx += 1
        if s[i] == "#":
            ans += chr(int(s[idx:i]) + 96)
            idx = i + 1
    while idx < len(s):
        ans += chr(int(s[idx]) + 96)
        idx += 1
    return ans
```

解法二（用数组模拟队列）：

```python
def freqAlphabets(self, s: str) -> str:
    ans = ""
    queue = []
    for i in range(len(s)):
        if len(queue) > 2:
            ans += chr(int(queue.pop(0)) + 96)
        if s[i] == "#":
            ans += chr(int(queue.pop(0) + queue.pop(0)) + 96)
        else:
            queue.append(s[i])
    while queue:
        ans += chr(int(queue.pop(0)) + 96)
    return ans
```