import collections
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        size1, size2 = len(matrix), len(matrix[0])

        count = collections.Counter()

        for i1 in range(size1):
            if matrix[i1][0] == 1:
                count[tuple(matrix[i1])] += 1
            else:
                count[tuple(1 if x == 0 else 0 for x in matrix[i1])] += 1

        return count.most_common(1)[0][1]


if __name__ == "__main__":
    # 1
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 1]]))

    # 2
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]))

    # 2
    print(Solution().maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))
