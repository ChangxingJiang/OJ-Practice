from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size = len(nums)

        ans = 0

        left = 0
        odd_num = 0
        even_left = 0
        for right in range(size):
            if nums[right] % 2 == 1:
                odd_num += 1
                if odd_num == k:
                    ans += even_left + 1
                elif odd_num > k:
                    odd_num -= 1
                    left += 1

                    even_left = 0
                    while nums[left] % 2 == 0:
                        even_left += 1
                        left += 1

                    ans += even_left + 1
            else:
                if odd_num == k:
                    ans += even_left + 1
                elif odd_num == 0:
                    left += 1
                    even_left += 1

        return ans


if __name__ == "__main__":
    print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))  # 2
    print(Solution().numberOfSubarrays(nums=[2, 4, 6], k=1))  # 0
    print(Solution().numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))  # 16
