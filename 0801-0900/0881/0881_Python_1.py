from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ans = 0

        i1, i2 = 0, len(people) - 1
        while i1 <= i2:
            while i1 < i2 and people[i1] + people[i2] > limit:
                i2 -= 1
                ans += 1
            i1 += 1
            i2 -= 1
            ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().numRescueBoats([1, 2], 3))  # 1
    print(Solution().numRescueBoats([3, 2, 2, 1], 3))  # 3
    print(Solution().numRescueBoats([3, 5, 3, 4], 5))  # 4
