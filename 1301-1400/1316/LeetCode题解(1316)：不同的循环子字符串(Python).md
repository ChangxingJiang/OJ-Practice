# LeetCode题解(1316)：字符串中包含的可以写为a+a(a为字符串)的子串数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/distinct-echo-substrings/)（困难）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^3)$   | 2472ms (63.86%) |
| Ans 2 (Python) | $O(N^3)$   | $O(N^3)$   | 1112ms (93.98%) |
| Ans 3 (Python) | $O(N^3)$   | $O(N^3)$   | 192ms (100.00%) |

解法一（暴力枚举法）：

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        ans = set()
        for i in range(N):
            for j in range(1, (N - i) // 2 + 1):
                if text[i:i + j] == text[i + j:i + 2 * j]:
                    ans.add(text[i:i + 2 * j])
        return len(ans)
```

解法二：

> 遍历所有作为重复值中点的坐标，并通过记录每个字符的位置减少遍历次数。

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        count = collections.defaultdict(collections.deque)
        ans = set()
        for i, ch in enumerate(text):
            for left in count[ch]:
                right = i + (i - left)
                if right > N:
                    break
                if text[left:i] == text[i:right]:
                    ans.add(text[left:right])
            count[ch].appendleft(i)
        return len(ans)
```

解法三（取巧）：

![LeetCode题解(1316)：截图1](LeetCode题解(1316)：截图1.png)

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)

        # 对特别消耗时间的特殊情况的处理
        if len(set(text)) == 1:
            return N // 2

        # 对常规情况的处理
        count = collections.defaultdict(collections.deque)
        ans = set()
        for i, ch in enumerate(text):
            for left in count[ch]:
                right = i + (i - left)
                if right > N:
                    break
                if text[left:i] == text[i:right]:
                    ans.add(text[left:right])
            count[ch].appendleft(i)
        return len(ans)
```