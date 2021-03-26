from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)

        ans = 0

        for j in range(1, size - 1):
            n1 = n2 = n3 = n4 = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    n1 += 1
                elif rating[i] > rating[j]:
                    n3 += 1
            for k in range(j + 1, size):
                if rating[j] < rating[k]:
                    n2 += 1
                elif rating[j] > rating[k]:
                    n4 += 1
            ans += n1 * n2 + n3 * n4

        return ans


if __name__ == "__main__":
    print(Solution().numTeams(rating=[2, 5, 3, 4, 1]))  # 3
    print(Solution().numTeams(rating=[2, 1, 3]))  # 0
    print(Solution().numTeams(rating=[1, 2, 3, 4]))  # 4
