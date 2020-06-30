from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        idx = 0
        wrong = False
        while idx < len(nums) - 1:
            if nums[idx] > nums[idx + 1]:
                if wrong:
                    print("两次错误")
                    return False
                else:
                    wrong = True
                    if idx > 0 and idx + 1 < len(nums) and nums[idx - 1] > nums[idx + 1]:
                        if idx + 2 < len(nums) and nums[idx] > nums[idx + 2]:
                            return False
            idx += 1
        else:
            return True


if __name__ == "__main__":
    print(Solution().checkPossibility([4, 2, 3]))  # True
    print(Solution().checkPossibility([4, 2, 1]))  # False
    print(Solution().checkPossibility([2, 3, 3, 2, 4]))  # True
    print(Solution().checkPossibility([3, 4, 2, 3]))  # False
