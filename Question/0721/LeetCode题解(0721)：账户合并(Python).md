# LeetCode题解(0721)：账户合并(Python)

题目：[原题链接](https://leetcode-cn.com/problems/accounts-merge/)（中等）

标签：并查集、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 272ms (61.28%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ans = []

        people_dic = {}
        mail_lst = set()
        for account in accounts:
            # 处理没有邮件地址的情况
            if len(account) == 1:
                ans.append(account)

            # 处理有邮件地址的情况
            for i in range(1, len(account)):
                mail_lst.add(account[i])
                people_dic[account[i]] = account[0]

        mail_lst = list(mail_lst)
        mail_dic1 = {mail: i for i, mail in enumerate(mail_lst)}
        mail_dic2 = {i: mail for i, mail in enumerate(mail_lst)}

        dsu = DSU(len(mail_lst))
        for account in accounts:
            if len(account) > 1:
                idx1 = mail_dic1[account[1]]
                for i in range(2, len(account)):
                    idx2 = mail_dic1[account[i]]
                    dsu.union(idx1, idx2)

        res_dic = collections.defaultdict(list)
        for i in range(len(mail_lst)):
            res_dic[dsu.find(i)].append(mail_dic2[i])

        ans = []
        for i, lst in res_dic.items():
            ans.append([people_dic[mail_dic2[i]]] + list(sorted(lst)))
        return ans
```