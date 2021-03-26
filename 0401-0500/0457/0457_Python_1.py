from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for i1, num in enumerate(nums):
            if i1 in visited:
                continue
            flag1 = 1 if nums[i1] > 0 else -1
            circle = set()
            i2 = i1
            while i2 not in circle:
                flag2 = 1 if nums[i2] > 0 else -1
                if flag1 != flag2:
                    break
                circle.add(i2)
                i2 = (i2 + nums[i2]) % len(nums)
            else:
                if len(circle) != 1 and i2 != (i2 + nums[i2]) % len(nums):  # 进入单个数字的循环
                    return True
            visited &= circle
        return False


if __name__ == "__main__":
    print(Solution().circularArrayLoop([2, -1, 1, 2, 2]))  # True
    print(Solution().circularArrayLoop([-1, 2]))  # False
    print(Solution().circularArrayLoop([-2, 1, -1, -2, -2]))  # False
    print(Solution().circularArrayLoop([-1, -2, -3, -4, -5]))  # False
