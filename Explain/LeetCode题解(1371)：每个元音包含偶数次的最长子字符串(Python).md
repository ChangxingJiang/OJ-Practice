# LeetCode题解(1371)：每个元音包含偶数次的最长子字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 超出时间限制    |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 1008ms (23.68%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 148ms (99.85%)  |

解法一（递归暴力解法）：

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 统计每个字母的数量
        count = collections.Counter(s)

        # 递归处理字母数量不为偶数的情况
        for ch in ["a", "e", "i", "o", "u"]:
            if count[ch] % 2 == 1:
                idx1 = s.index(ch)
                idx2 = s.rindex(ch)
                return max(self.findTheLongestSubstring(s[:idx2]), self.findTheLongestSubstring(s[idx1 + 1:]))

        # 若均为偶数则返回当前字符串长度
        return len(s)
```

解法二（前缀和）：

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        now = [True, True, True, True, True]  # 当前状态
        hashmap = {tuple(now): -1}
        ans = 0
        for i, ch in enumerate(s):
            # 更新当前状态
            if ch == "a":
                now[0] = not now[0]
            elif ch == "e":
                now[1] = not now[1]
            elif ch == "i":
                now[2] = not now[2]
            elif ch == "o":
                now[3] = not now[3]
            elif ch == "u":
                now[4] = not now[4]

            # 判断当前状态的最长子串
            this = tuple(now)
            if this in hashmap:
                ans = max(ans, i - hashmap[this])
            else:
                hashmap[this] = i
        return ans
```

解法三（优化解法二）：

> * 使用二进制数存储状态
> * 减少判断次数

![LeetCode题解(1371)：截图1](LeetCode题解(1371)：截图1.png)

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hashmap = {0: -1}
        now = 0  # 当前状态
        ans = 0
        for i, ch in enumerate(s):
            if ch in {"a", "e", "i", "o", "u"}:
                # 判断当前状态的最长子串
                if now in hashmap:
                    ans = max(ans, i - hashmap[now] - 1)

                # 更新当前状态
                if ch == "a":
                    now ^= 16
                elif ch == "e":
                    now ^= 8
                elif ch == "i":
                    now ^= 4
                elif ch == "o":
                    now ^= 2
                elif ch == "u":
                    now ^= 1

                # 记录新状态的位置
                if now not in hashmap:
                    hashmap[now] = i
        if now in hashmap:
            ans = max(ans, len(s) - hashmap[now] - 1)
        return ans
```

