from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()

        s1, s2 = len(staple), len(drinks)

        i2 = 0
        while i2 < s2 and staple[0] + drinks[i2] <= x:
            i2 += 1

        ans = 0
        for i1 in range(s1):
            while i2 > 0 and staple[i1] + drinks[i2 - 1] > x:
                i2 -= 1
            ans += i2

        return ans % 1000000007


if __name__ == "__main__":
    # 6
    print(Solution().breakfastNumber(staple=[10, 20, 5], drinks=[5, 5, 2], x=15))

    # 8
    print(Solution().breakfastNumber(staple=[2, 1, 1], drinks=[8, 9, 5, 1], x=9))
