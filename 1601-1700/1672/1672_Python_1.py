from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)


if __name__ == "__main__":
    print(Solution().maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))  # 6
    print(Solution().maximumWealth(accounts = [[1,5],[7,3],[3,5]]))  # 10
    print(Solution().maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))  # 17
