from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        size1, size2 = len(nums1), len(nums2)
        dp = [0] * size1  # 左侧每个数字匹配到的位置

        ans = []
        for _ in range(min(size1 * size2, k)):
            min_i1, min_val = -1, float("inf")
            for i1 in range(size1):
                i2 = dp[i1]
                if i2 < size2:
                    val = nums1[i1] + nums2[i2]
                    if val < min_val:
                        min_i1, min_val = i1, val
                    # elif val == min_val:
                    #     min_idx.append(i1)

            ans.append([nums1[min_i1], nums2[dp[min_i1]]])
            dp[min_i1] += 1

        return ans


if __name__ == "__main__":
    # [1,2],[1,4],[1,6]
    print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))

    # [1,1],[1,1]
    print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))

    # [1,3],[2,3]
    print(Solution().kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
