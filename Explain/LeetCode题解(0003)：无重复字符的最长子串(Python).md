# LeetCode题解(0003)：字符串中无重复字符的最长子串(Python)

题目：[题目链接](https://leetcode-cn.com/problems/add-two-numbers/)（中等）

标签：字符串、双指针、哈希表、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 3356ms (>5.01%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 44ms (>99.97%)  |

解法一（分别计算以每个字为起点的最长无重复子串）：

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    for i in range(len(s)):
        hashset = set()
        sub_ans = len(s) - i
        for j in range(len(s[i:])):
            if s[i:][j] in hashset:
                sub_ans = j
                break
            hashset.add(s[i:][j])
        if sub_ans > ans:
            ans = sub_ans
    return ans
```

解法二（分别判断以每个字为结束的最长无重复子串；即遇到重复的字符，则判断是否移动起始下标的位置）：

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    hashmap = {}  # 距离当前位置最近的字符坐标
    now = 0  # 当前长度
    for i, ch in enumerate(s):
        now += 1
        if ch in hashmap:
            now = min(now, i - hashmap[ch])
        hashmap[ch] = i
        ans = max(ans, now)
    return ans
```

