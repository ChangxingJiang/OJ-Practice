import collections
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        size = len(hand)

        if size % W != 0:
            return False

        def get_num(nums):
            lst = [0] * (len(nums) + 1)
            now = 0
            for i in range(len(nums)):
                if nums[i] > now:
                    lst[i] += (nums[i] - now)
                    if i + W > len(nums):
                        return False
                    lst[i + W - 1] -= (nums[i] - now)
                now += lst[i]
            return now == 0

        count = collections.Counter(hand)

        now_val = []
        now_num = []
        for v in sorted(count):
            if not now_val or now_val[-1] == v - 1:
                now_val.append(v)
                now_num.append(count[v])
            else:
                if not get_num(now_num):
                    return False
                now_val, now_num = [v], [count[v]]

        if not get_num(now_num):
            return False

        return True


if __name__ == "__main__":
    print(Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3))  # True
    print(Solution().isNStraightHand(hand=[1, 2, 3, 4, 5], W=4))  # False
