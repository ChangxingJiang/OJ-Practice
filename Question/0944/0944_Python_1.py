from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        size = len(A)
        ans = 0
        for j in range(len(A[0])):
            for i in range(1, size):
                if A[i - 1][j] > A[i][j]:
                    ans += 1
                    break
        return ans


if __name__ == "__main__":
    print(Solution().minDeletionSize(["cba", "daf", "ghi"]))  # 1
    print(Solution().minDeletionSize(["a", "b"]))  # 0
    print(Solution().minDeletionSize(["zyx", "wvu", "tsr"]))  # 3
