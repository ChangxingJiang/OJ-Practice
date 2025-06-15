from collections import Counter
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        prefix = []  # 计算每个数前面该数 2 倍的数量
        prefix_hash = Counter()  # 计算前面每个数的出现次数
        for num in nums:
            prefix.append(prefix_hash[num * 2])
            prefix_hash[num] += 1

        suffix = []  # 计算每个数后面该数 2 倍的数量
        suffix_hash = Counter()  # 计算后面每个数的出现次数
        for num in nums[::-1]:
            suffix.append(suffix_hash[num * 2])
            suffix_hash[num] += 1
        suffix.reverse()

        # 计算最终结果
        n = len(nums)
        result = 0
        for i in range(n):
            result = (result + prefix[i] * suffix[i]) % MOD
        return result


if __name__ == "__main__":
    print(Solution().specialTriplets([6, 3, 6]))  # 1
    print(Solution().specialTriplets([0, 1, 0, 0]))  # 1
    print(Solution().specialTriplets([8, 4, 2, 8, 4]))  # 2
