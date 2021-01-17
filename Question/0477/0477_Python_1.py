from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = [0] * 31  # 10**9 < 2*30
        size = len(nums)
        max_length = 0

        for num in nums:
            length = num.bit_length()
            max_length = max(max_length, length)
            for i in range(length):
                if num & (1 << i):
                    count[i] += 1

        return sum(n * (size - n) for n in count)


if __name__ == "__main__":
    print(Solution().totalHammingDistance([4, 14, 2]))  # 6
