from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = max(nums).bit_length()
        max_xor = 0
        for i in range(length)[::-1]:
            # 将上一位的最大异或值左移位
            max_xor <<= 1

            # 当前位目标最大异或值
            curr_xor = max_xor | 1

            # 计算每个数值当前长度的前缀
            prefixes = {num >> i for num in nums}

            # 如果确实找到了可以实现当前位目标最大异或值的值
            if any(curr_xor ^ p in prefixes for p in prefixes):
                max_xor |= 1

        return max_xor


if __name__ == "__main__":
    print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))  # 28
