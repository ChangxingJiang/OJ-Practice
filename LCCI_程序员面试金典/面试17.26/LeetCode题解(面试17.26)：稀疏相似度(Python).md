# LeetCode题解(面试17.26)：稀疏相似度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sparse-similarity-lcci/)（困难）

标签：哈希表

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时        |
| -------------- | -------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(D^2×L^2)$   | $O(D×L)$   | 1632ms (56.98%) |
| Ans 2 (Python) | $O(D×L+C×D^2)$ | $O(D×L)$   | 776ms (59.78%)  |
| Ans 3 (Python) |                |            |                 |

其中D为文章数、L为文章长度、C为共现词总数

解法一（暴力解法）：

```python
class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        size = len(docs)
        docs = [set(doc) for doc in docs]

        ans = []

        for i in range(size):
            for j in range(i + 1, size):
                s = len(docs[i] & docs[j]) / len(docs[i] | docs[j])
                if s > 0:
                    ans.append("{0:},{1:}: {2:.4f}".format(i, j, s + 1e-9))

        return ans
```

解法二（先寻找相似位置）：

```python
class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        size = len(docs)

        # 寻找文章中的词频
        # O(D×L)
        count_doc = collections.defaultdict(list)
        for i, doc in enumerate(docs):
            for word in set(doc):
                count_doc[word].append(i)

        # 寻找文章中的共现词
        # O(C×D^2)
        count_co = collections.Counter()
        for lst in count_doc.values():
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    count_co[(lst[i], lst[j])] += 1

        ans = []

        # 计算结果
        # O(D^2)
        for i in range(size):
            for j in range(i + 1, size):
                co = count_co[(i, j)]
                s = co / (len(docs[i]) + len(docs[j]) - co)
                if s > 0:
                    ans.append("{0:},{1:}: {2:.4f}".format(i, j, s + 1e-9))

        return ans
```