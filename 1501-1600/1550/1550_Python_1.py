from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        num = 0
        for n in arr:
            if n % 2 == 1:
                num += 1
                if num == 3:
                    return True
            else:
                num = 0
        return False


if __name__ == "__main__":
    print(Solution().threeConsecutiveOdds(arr=[2, 6, 4, 1]))  # False
    print(Solution().threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))  # True
