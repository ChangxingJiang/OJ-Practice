from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i1, i2 = 0, 0
        while i1 < len(A) and i2 < len(B):
            left = max(A[i1][0], B[i2][0])
            right = min(A[i1][1], B[i2][1])
            if left <= right:
                ans.append([left, right])

            if A[i1][1] < B[i2][1]:
                i1 += 1
            else:
                i2 += 1

        return ans


if __name__ == "__main__":
    # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print(Solution().intervalIntersection(A=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                          B=[[1, 5], [8, 12], [15, 24], [25, 26]]))
