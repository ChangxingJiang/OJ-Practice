from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        size = len(A)

        idx2 = 0
        while idx2 < size and A[idx2] < 0:
            idx2 += 1
        idx1 = idx2 - 1

        ans = []
        while 0 <= idx1 and idx2 <= size - 1:
            p1 = A[idx1] ** 2
            p2 = A[idx2] ** 2
            if p1 < p2:
                ans.append(p1)
                idx1 -= 1
            else:
                ans.append(p2)
                idx2 += 1

        while 0 <= idx1:
            ans.append(A[idx1] ** 2)
            idx1 -= 1

        while idx2 <= size - 1:
            ans.append(A[idx2] ** 2)
            idx2 += 1

        return ans


if __name__ == "__main__":
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))  # [4,9,9,49,121]
