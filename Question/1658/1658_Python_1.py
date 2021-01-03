from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 寻找处理方案
        last = 0
        count_left = {0: 0}
        for i, n in enumerate(nums):
            last += n
            count_left[last] = i + 1

        # print(count_left)

        choose = []

        last = 0
        for i, n in enumerate(nums[::-1]):
            aim = x - last
            if aim in count_left:
                if count_left[aim] + i <= len(nums):
                    choose.append((count_left[aim], i))
            last += n

        # 寻找操作数最少的处理方案
        if not choose:
            return -1
        choose.sort(key=lambda k: k[0] + k[1])

        # print(choose)

        # 处理字符串并返回结果
        ans = choose[0]

        nums[:] = nums[ans[0]:-ans[1]]

        # print(nums)

        return ans[0] + ans[1]


if __name__ == "__main__":
    print(Solution().minOperations(nums=[1, 1], x=3))  # -1
    print(Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5))  # 2
    print(Solution().minOperations(nums=[5, 6, 7, 8, 9], x=4))  # -1
    print(Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))  # 5
