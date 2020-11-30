from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_val = max(nums)  # O(N)
        now = 1

        while (10 ** (now - 1)) <= max_val:
            v1, v2 = 10 ** now, 10 ** (now - 1)

            # 生成桶：O(N)
            buckets = [[] for _ in range(10)]
            for n in nums:
                buckets[n % v1 // v2].append(n)

            # 合并桶：O(N)
            nums = []
            for bucket in buckets:
                nums.extend(bucket)

            now += 1

        # 计算结果：O(N)
        ans = 0
        for i in range(len(nums) - 1):
            ans = max(ans, nums[i + 1] - nums[i])
        return ans


if __name__ == "__main__":
    print(Solution().maximumGap([3, 6, 9, 1]))
    print(Solution().maximumGap([10]))
