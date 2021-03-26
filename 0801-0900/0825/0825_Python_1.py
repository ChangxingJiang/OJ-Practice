from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for age1, n1 in enumerate(count):
            for age2, n2 in enumerate(count):
                if age1 * 0.5 + 7 >= age2:
                    continue
                if age1 < age2:
                    continue
                if age1 < 100 < age2:
                    continue

                if age1 == age2:
                    ans += n1 * (n1 - 1)
                else:
                    ans += n1 * n2

        return ans


if __name__ == "__main__":
    print(Solution().numFriendRequests([16, 16]))  # 2
    print(Solution().numFriendRequests([16, 17, 18]))  # 2
    print(Solution().numFriendRequests([20, 30, 100, 110, 120]))  # 3
    print(Solution().numFriendRequests([73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]))  # 29
