# LeetCode题解(面试17.07)：婴儿名字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/baby-names-lcci/)（中等）

标签：并查集、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 440ms (45.14%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（并查集）：

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
        if i < j:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        count = collections.Counter()
        for name in names:
            word, num = name[:-1].split("(")
            count[word] = int(num)

        sorted_name = list(sorted(count.keys()))
        hashmap = {name: i for i, name in enumerate(sorted_name)}

        dsu = DSU(len(sorted_name))

        for synonym in synonyms:
            name1, name2 = synonym[1:-1].split(",")
            if name1 in hashmap and name2 in hashmap:
                dsu.union(hashmap[name1], hashmap[name2])

        res = collections.Counter()
        for i, name in enumerate(sorted_name):
            res[sorted_name[dsu.find(i)]] += count[name]

        ans = []
        for name in res.keys():
            ans.append("{}({})".format(name, res[name]))
        return ans
```