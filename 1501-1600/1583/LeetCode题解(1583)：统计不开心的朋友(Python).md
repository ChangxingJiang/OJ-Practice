# LeetCode题解(1583)：统计配对后不开心的朋友数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-unhappy-friends/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 96ms (67%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # 使用哈希表存储分组关系
        group_dict = {}
        for pair in pairs:
            group_dict[pair[0]] = pair[1]
            group_dict[pair[1]] = pair[0]

        # 使用哈希表存储亲近程度
        preference_dict = {}
        for i in range(n):
            friends = {}
            for j in range(n):
                if j == i:
                    continue
                elif j > i:
                    j -= 1
                friends[preferences[i][j]] = j
            preference_dict[i] = friends

        ans = 0
        for pair in pairs:
            f1, f2 = pair[0], pair[1]
            for ff1 in preferences[f1]:
                if ff1 == f2:  # 处理已经遍历到配对队友的情况
                    break
                elif preference_dict[ff1][f1] < preference_dict[ff1][group_dict[ff1]]:  # 判断更喜欢的朋友是否更喜欢自己
                    ans += 1
                    break
            for ff1 in preferences[f2]:
                if ff1 == f1:  # 处理已经遍历到配对队友的情况
                    break
                elif preference_dict[ff1][f2] < preference_dict[ff1][group_dict[ff1]]:  # 判断更喜欢的朋友是否更喜欢自己
                    ans += 1
                    break

        return ans
```