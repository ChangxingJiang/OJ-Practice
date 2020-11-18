from typing import List


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        pass


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
