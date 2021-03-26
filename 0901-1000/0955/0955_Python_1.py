from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])

        ans = 0
        same_list = {i for i in range(m - 1)}
        for j in range(n):
            remove_list = set()
            for i in range(m - 1):
                if A[i][j] > A[i + 1][j] and i in same_list:
                    ans += 1
                    break
                elif A[i][j] < A[i + 1][j]:
                    if i in same_list:
                        remove_list.add(i)
            else:
                if not same_list:
                    return ans
                same_list -= remove_list

        return ans


if __name__ == "__main__":
    print(Solution().minDeletionSize(["ca", "bb", "ac"]))  # 1
    print(Solution().minDeletionSize(["xc", "yb", "za"]))  # 0
    print(Solution().minDeletionSize(["zyx", "wvu", "tsr"]))  # 3
    print(Solution().minDeletionSize(["xga", "xfb", "yfa"]))  # 1
    print(Solution().minDeletionSize(["doeeqiy", "yabhbqe", "twckqte"]))  # 3
