from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}  # 定义桶
        bucket_size = t + 1  # 定义桶的大小

        for i in range(len(nums)):
            # 计算需要放入的桶编号
            bucket_idx = nums[i] // bucket_size

            # 如果桶已经存在，则返回True
            if bucket_idx in buckets:
                return True

            # 将数据放入到桶中
            buckets[bucket_idx] = nums[i]

            # 如果前一个桶已经存在符合要求的值，则返回True
            if (bucket_idx - 1) in buckets and abs(buckets[bucket_idx - 1] - nums[i]) <= t:
                return True

            # 如果后一个桶已经存在符合要求的值，则返回True
            if (bucket_idx + 1) in buckets and abs(buckets[bucket_idx + 1] - nums[i]) <= t:
                return True

            # 如果没有符合要求的值，且桶的数量已经满了，则移除最老的桶
            if i >= k:
                buckets.pop(nums[i - k] // bucket_size)

        return False


if __name__ == "__main__":
    # True
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))

    # True
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))

    # False
    print(Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
