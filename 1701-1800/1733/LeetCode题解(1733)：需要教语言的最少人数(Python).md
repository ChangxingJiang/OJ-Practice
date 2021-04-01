# LeetCode题解(1733)：需要教语言的最少人数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-people-to-teach/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(L+F)$   | $O(L+N)$   | 140ms (97.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        need_friends = set()  # 需要学习语言才能交流的好友列表

        languages = [set(language) for language in languages]

        for u, v in friendships:
            if not languages[u - 1] & languages[v - 1]:
                need_friends.add(u)
                need_friends.add(v)

        language_knows_num = [0] * n  # 每种语言在需要学习语言的好友中已学习的数量
        for friend in need_friends:
            for i in languages[friend - 1]:
                language_knows_num[i - 1] += 1

        return len(need_friends) - max(language_knows_num)
```

