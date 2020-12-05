from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print(Solution().intervalIntersection(A=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                          B=[[1, 5], [8, 12], [15, 24], [25, 26]]))
