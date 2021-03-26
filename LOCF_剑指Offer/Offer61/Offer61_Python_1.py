from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        cards = sorted(filter(lambda x: x != 0, nums))
        king_num = nums.count(0)

        for i in range(len(cards) - 1):
            num = cards[i + 1] - cards[i]
            if num == 0:
                return False
            if num > 1:
                king_num -= num - 1
                if king_num < 0:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().isStraight([1, 2, 3, 4, 5]))  # True
    print(Solution().isStraight([0, 0, 1, 2, 5]))  # True
