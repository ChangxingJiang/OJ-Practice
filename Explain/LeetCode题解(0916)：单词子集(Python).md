# LeetCode题解(0916)：判断单词是否包含指定多个子集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-subsets/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+M)$   | $O(N+M)$   | 960ms (70.08%) |
| Ans 2 (Python) | $O(N+M)$   | $O(N+M)$   | 572ms (99.21%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 整理子集列表
        count = collections.Counter()
        for b in B:
            tmp = collections.Counter(b)
            for key, value in tmp.items():
                count[key] = max(count[key], value)

        # 筛选单词
        ans = []
        for a in A:
            tmp = collections.Counter(a)
            for key, value in count.items():
                if count[key] > tmp[key]:
                    break
            else:
                ans.append(a)

        return ans
```

解法二（解法一效率优化）：

![LeetCode题解(0916)：截图1](LeetCode题解(0916)：截图1.png)

```python
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 整理子集列表
        count = {}
        for b in B:
            tmp = {}
            for ch in b:
                if ch not in tmp:
                    tmp[ch] = 1
                else:
                    tmp[ch] += 1
                if ch not in count:
                    count[ch] = 1
                else:
                    count[ch] = tmp[ch] if tmp[ch] > count[ch] else count[ch]

        # 生成模式
        s = []
        for ch in count:
            s.append(ch * count[ch])
        s = "".join(s)

        # 筛选单词
        ans = []
        for a in A:
            ans.append(a)
            for ch in s:
                if ch in a:
                    a = a.replace(ch, "", 1)
                else:
                    break
            else:
                continue
            ans.pop()
        return ans
```