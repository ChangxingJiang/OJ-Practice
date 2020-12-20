from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        n1, n2 = nums[0], nums[1]
        if n2 > n1:
            now = 1
            ans = 2
        elif n2 < n1:
            now = -1
            ans = 2
        else:
            now = 0
            ans = 1

        for i in range(2, len(nums)):
            if now == 1:
                if nums[i] >= n2:
                    n2 = nums[i]
                else:
                    n1, n2 = n2, nums[i]
                    now = -1
                    ans += 1
            elif now == -1:
                if nums[i] <= n2:
                    n2 = nums[i]
                else:
                    n1, n2 = n2, nums[i]
                    now = 1
                    ans += 1
            else:
                if nums[i] > n2:
                    n2 = nums[i]
                    now = 1
                    ans += 1
                elif nums[i] < n2:
                    n2 = nums[i]
                    now = -1
                    ans += 1

        return ans


if __name__ == "__main__":
    # 6
    print(Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]))

    # 7
    print(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))

    # 2
    print(Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
