from typing import List


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        size = len(docs)
        docs = [set(doc) for doc in docs]

        ans = []

        for i in range(size):
            for j in range(i + 1, size):
                co = len(docs[i] & docs[j])
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
