from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        size = len(customers)
        ans = 0

        now = 0
        for arrival, time in customers:
            if now < arrival:
                ans += time
                now = arrival + time
            else:
                ans += (now - arrival) + time
                now += time

        return ans / size


if __name__ == "__main__":
    print(Solution().averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]))  # 5.00000
    print(Solution().averageWaitingTime(customers=[[5, 2], [5, 4], [10, 3], [20, 1]]))  # 3.25000
