# LeetCode题解(1152)：用户网站访问行为分析(Python)

题目：[原题链接](https://leetcode-cn.com/problems/analyze-user-website-visit-pattern/)（中等）

标签：哈希表、数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^3)$   | 72ms (50.98%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        size1 = len(username)

        # 依据用户整理
        # O(N)
        count1 = collections.defaultdict(list)
        for i in range(size1):
            user, time, site = username[i], timestamp[i], website[i]
            count1[user].append((time, site))

        count2 = collections.defaultdict(list)
        for user, lst in count1.items():
            count2[user] = [i[1] for i in sorted(lst)]

        # 依据路径整理
        count3 = collections.Counter()
        for lst in count2.values():
            paths = set()
            size2 = len(lst)
            for i in range(size2):
                for j in range(i + 1, size2):
                    for k in range(j + 1, size2):
                        paths.add((lst[i], lst[j], lst[k]))
            # 每个用户去重
            for path in paths:
                count3[path] += 1

        # 返回结果
        ans = list(count3.keys())
        ans.sort(key=lambda x: (-count3[x], x))

        return list(ans[0])
```