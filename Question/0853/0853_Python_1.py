from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(position)
        lst = [(position[i], speed[i]) for i in range(size)]
        lst.sort(reverse=True)

        ans = 0
        last = 0
        for position, speed in lst:
            now = (target - position) / speed
            if now > last:
                ans += 1
            last = max(last, now)

        return ans


if __name__ == "__main__":
    # 3
    print(Solution().carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
