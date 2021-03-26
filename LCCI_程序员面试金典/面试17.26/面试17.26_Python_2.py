import collections
from typing import List


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
        # O(D×C^2)
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


if __name__ == "__main__":
    # [
    #   "0,1: 0.2500",
    #   "0,2: 0.1000",
    #   "2,3: 0.1429"
    # ]
    print(Solution().computeSimilarities([
        [14, 15, 100, 9, 3],
        [32, 1, 9, 3, 5],
        [15, 29, 2, 6, 8, 7],
        [7, 10]
    ]))
