from typing import List
import collections


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        size = len(nums)

        if size % k != 0:
            return False

        def get_num(nums):
            lst = [0] * (len(nums) + 1)
            now = 0
            for i in range(len(nums)):
                if nums[i] > now:
                    lst[i] += (nums[i] - now)
                    if i + k > len(nums):
                        return False
                    lst[i + k - 1] -= (nums[i] - now)
                now += lst[i]
            return now == 0

        count = collections.Counter(nums)

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
    print(Solution().isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))  # True
    print(Solution().isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3))  # True
    print(Solution().isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))  # True
    print(Solution().isPossibleDivide(nums=[3, 3, 2, 2, 1, 1], k=3))  # False
