from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        # 计算前缀和
        prefix = []
        now = 0
        for n in nums:
            now += n
            prefix.append(now)

        size = len(nums)

        if size < 7:
            return False

        for i1 in range(3, size - 3):
            choices = set()
            for i2 in range(1, i1 - 1):
                if prefix[i2 - 1] == prefix[i1 - 1] - prefix[i2]:
                    choices.add(prefix[i2 - 1])
            for i2 in range(i1 + 2, size - 1):
                if prefix[i2 - 1] - prefix[i1] == prefix[-1] - prefix[i2] and (prefix[i2 - 1] - prefix[i1]) in choices:
                    return True

        return False


if __name__ == "__main__":
    print(Solution().splitArray([1, 2, 1, 2, 1, 2, 1]))  # True
    print(Solution().splitArray([1, 2, -1, 1, 2, 5, 2, 5, 2]))  # True
    print(Solution().splitArray([1, 2, -1, 1, 2, 5, 2, 5, 2]))  # True
