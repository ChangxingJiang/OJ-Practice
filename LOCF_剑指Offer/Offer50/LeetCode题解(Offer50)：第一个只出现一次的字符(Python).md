# LeetCode题解(Offer50)：寻找字符串中第一个只出现一次的字符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 76ms (96.79%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 92ms (79.46%) |
| Ans 3 (Python) |            |            |               |

解法一（哈希表）：

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        order = []
        more = set()
        maybe = set()
        for ch in s:
            if ch not in more:
                if ch in maybe:
                    maybe.remove(ch)
                    more.add(ch)
                else:
                    order.append(ch)
                    maybe.add(ch)

        ans = sorted(maybe, key=lambda x: order.index(x))

        return ans[0] if ans else " "
```

解法二（有序哈希表）：

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for ch in s:
            if ch in dic:
                dic[ch] = False
            else:
                dic[ch] = True

        for ch, val in dic.items():
            if val:
                return ch

        return " "
```