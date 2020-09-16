from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def helper(n):
            return mat[n].count(1), n

        m = [i for i in range(len(mat))]
        m.sort(key=helper)

        return m[:k]


if __name__ == "__main__":
    # [2,0,3]
    print(Solution().kWeakestRows(mat=[[1, 1, 0, 0, 0],
                                       [1, 1, 1, 1, 0],
                                       [1, 0, 0, 0, 0],
                                       [1, 1, 0, 0, 0],
                                       [1, 1, 1, 1, 1]],
                                  k=3))

    # [0,2]
    print(Solution().kWeakestRows(mat=[[1, 0, 0, 0],
                                       [1, 1, 1, 1],
                                       [1, 0, 0, 0],
                                       [1, 0, 0, 0]],
                                  k=2))
