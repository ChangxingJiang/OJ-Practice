from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_val = 0
        max_step = -1
        money = 0
        wait = 0
        i = 0
        while i < len(customers) or wait > 0:
            people = customers[i] if i < len(customers) else 0
            money -= runningCost
            wait += people
            if wait >= 4:
                money += boardingCost * 4
                wait -= 4
                if money > max_val:
                    max_val = money
                    max_step = i + 1
            elif wait > 0:
                money += boardingCost * wait
                wait = 0
                if money > max_val:
                    max_val = money
                    max_step = i + 1
            i += 1
        return max_step


if __name__ == "__main__":
    print(Solution().minOperationsMaxProfit(customers=[8, 3], boardingCost=5, runningCost=6))  # 3
    print(Solution().minOperationsMaxProfit(customers=[10, 9, 6], boardingCost=6, runningCost=4))  # 7
    print(Solution().minOperationsMaxProfit(customers=[3, 4, 0, 5, 1], boardingCost=1, runningCost=92))  # -1
    print(Solution().minOperationsMaxProfit(customers=[10, 10, 6, 4, 7], boardingCost=3, runningCost=8))  # 9
