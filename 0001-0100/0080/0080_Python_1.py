from typing import List


class Solution:
    _SMALL = -10001

    def removeDuplicates(self, nums: List[int]) -> int:
        i1 = 0
        now_val, now_num = self._SMALL, 0
        for i2 in range(len(nums)):
            if nums[i2] != now_val:
                nums[i1] = nums[i2]
                now_val, now_num = nums[i2], 1
                i1 += 1
            elif now_num < 2:
                nums[i1] = nums[i2]
                now_num += 1
                i1 += 1
            else:
                now_num += 1
        nums[i1:] = []
        return len(nums)


if __name__ == "__main__":
    lst = [1, 1, 1, 2, 2, 3]
    print(Solution().removeDuplicates(lst))  # 5
    print(lst)  # [1,1,2,2,3]

    lst = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(Solution().removeDuplicates(lst))  # 7
    print(lst)  # [0,0,1,1,2,3,3]
