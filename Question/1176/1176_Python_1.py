from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        now = 0
        for i in range(k):
            now += calories[i]

        lst = [now]

        for i in range(len(calories) - k):
            now -= calories[i]
            now += calories[i + k]
            lst.append(now)

        ans = 0

        for v in lst:
            if v < lower:
                ans -= 1
            elif v > upper:
                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3))  # 0
    print(Solution().dietPlanPerformance(calories=[3, 2], k=2, lower=0, upper=1))  # 1
    print(Solution().dietPlanPerformance(calories=[6, 5, 0, 0], k=2, lower=1, upper=5))  # 0
