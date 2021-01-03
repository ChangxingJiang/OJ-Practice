from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        pass


if __name__ == "__main__":
    print(Solution().averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]))  # 5.00000
    print(Solution().averageWaitingTime(customers=[[5, 2], [5, 4], [10, 3], [20, 1]]))  # 3.25000
