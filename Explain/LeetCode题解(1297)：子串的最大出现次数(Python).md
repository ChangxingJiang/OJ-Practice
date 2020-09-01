# LeetCode题解(1297)：寻找符合特定条件且出现次数最大的子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-occurrences-of-a-substring/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度                         | 空间复杂度                         | 执行用时       |
| -------------- | ---------------------------------- | ---------------------------------- | -------------- |
| Ans 1 (Python) | $O(N×L)$ : 其中$L=maxSize-minSize$ | $O(N×L)$ : 其中$L=maxSize-minSize$ | 超出时间限制   |
| Ans 2 (Python) | $O(N)$                             | $O(N)$                             | 256ms (46.34%) |
| Ans 3 (Python) | $O(NlogN)$                         | $O(N)$                             | 152ms (98.17%) |

解法一（暴力解法）：

```python
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = []
        for length in range(minSize, maxSize + 1):
            lst = [0] * 26
            now = 0
            for i in range(len(s)):
                if i < length:
                    idx = ord(s[i]) - 97
                    if lst[idx] == 0:
                        now += 1
                    lst[idx] += 1
                else:
                    idx = ord(s[i]) - 97
                    if lst[idx] == 0:
                        now += 1
                    lst[idx] += 1
                    idx = ord(s[i - length]) - 97
                    lst[idx] -= 1
                    if lst[idx] == 0:
                        now -= 1
                if now <= maxLetters and i >= length - 1:
                    res.append(s[i - length + 1:i + 1])
                    
        ans = 0
        for elem in set(res):
            ans = max(ans, res.count(elem))
        return ans
```

解法二（优化解法一）：

> 短子串一定包含于场字符串中，因此只需要遍历最短的即可。

```python
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter()
        lst = [0] * 26
        now = 0
        for i in range(len(s)):
            if i < minSize:
                idx = ord(s[i]) - 97
                if lst[idx] == 0:
                    now += 1
                lst[idx] += 1
            else:
                idx = ord(s[i]) - 97
                if lst[idx] == 0:
                    now += 1
                lst[idx] += 1
                idx = ord(s[i - minSize]) - 97
                lst[idx] -= 1
                if lst[idx] == 0:
                    now -= 1
            if now <= maxLetters and i >= minSize - 1:
                res[s[i - minSize + 1:i + 1]] += 1

        return res.most_common(1)[0][1] if res else 0
```

解法三（优化解法二）：

> 先完整遍历再检查字符数量是否符合

```python
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter()
        for i in range(len(s) - minSize + 1):
            res[s[i:i + minSize]] += 1
        for elem, num in res.most_common():
            if len(set(elem)) <= maxLetters:
                return num
        return 0
```