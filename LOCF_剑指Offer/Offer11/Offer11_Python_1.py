from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1

        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1

        return numbers[left]


if __name__ == "__main__":
    print(Solution().minArray([3, 4, 5, 1, 2]))  # 1
    print(Solution().minArray([2, 2, 2, 0, 1]))  # 0
    print(Solution().minArray([1, 3, 5]))  # 1
    print(Solution().minArray([3, 1]))  # 1
    print(Solution().minArray([10, 1, 10, 10, 10]))  # 1
