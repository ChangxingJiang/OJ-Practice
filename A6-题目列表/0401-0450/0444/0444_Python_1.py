from typing import List


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    # False
    print(Solution().sequenceReconstruction(org=[1, 2, 3], seqs=[[1, 2], [1, 3]]))

    # False
    print(Solution().sequenceReconstruction(org=[1, 2, 3], seqs=[[1, 2]]))

    # True
    print(Solution().sequenceReconstruction(org=[1, 2, 3], seqs=[[1, 2], [1, 3], [2, 3]]))

    # True
    print(Solution().sequenceReconstruction(org=[4, 1, 5, 2, 6, 3], seqs=[[5, 2, 6, 3], [4, 1, 5, 2]]))
