# LeetCode题解(1452)：收藏清单(Python)

题目：[原题链接](https://leetcode-cn.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)（中等）

标签：集合

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 56ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（暴力解法）：

![LeetCode题解(1452)：截图](LeetCode题解(1452)：截图.png)

```python
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(favoriteCompany) for favoriteCompany in favoriteCompanies]
        ans = []
        for i, favoriteCompany1 in enumerate(favoriteCompanies):
            for favoriteCompany2 in favoriteCompanies:
                if favoriteCompany1 < favoriteCompany2:
                    break
            else:
                ans.append(i)
        return ans
```