from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        ans = 0
        last = timeSeries[0]
        for i in range(1, len(timeSeries)):
            time = timeSeries[i]
            ans += min((time - last), duration)
            last = time
        return ans + duration


if __name__ == "__main__":
    print(Solution().findPoisonedDuration([1, 4], 2))  # 2
    print(Solution().findPoisonedDuration([1, 2], 2))  # 3
