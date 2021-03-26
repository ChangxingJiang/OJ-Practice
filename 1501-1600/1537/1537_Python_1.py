from typing import List


# 数组 哈希表
# $O(N1+N2)$
# 双指针


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # 计算所有交叉路口（共存的值）
        # O(N1+N2)
        sets1 = set(nums1)
        cross = [n for n in nums2 if n in sets1]

        # 遍历计算两个数组到各个交叉路口的路径和
        # O(N1+N2)
        distances_1 = []
        idx = 0
        now = 0
        for num1 in nums1:
            if idx < len(cross) and num1 == cross[idx]:
                distances_1.append(now)
                now = 0
                idx += 1
            else:
                now += num1
        distances_1.append(now)

        distances_2 = []
        idx = 0
        now = 0
        for num2 in nums2:
            if idx < len(cross) and num2 == cross[idx]:
                distances_2.append(now)
                now = 0
                idx += 1
            else:
                now += num2
        distances_2.append(now)

        # 计算最终的最大值
        # O(CROSS) CROSS为交汇点数量
        ans = sum(cross)
        for i in range(len(distances_1)):
            ans += max(distances_1[i], distances_2[i])

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().maxSum(nums1=[2, 4, 5, 8, 10], nums2=[4, 6, 8, 9]))  # 30
    print(Solution().maxSum(nums1=[1, 3, 5, 7, 9], nums2=[3, 5, 100]))  # 109
    print(Solution().maxSum(nums1=[1, 2, 3, 4, 5], nums2=[6, 7, 8, 9, 10]))  # 40
    print(Solution().maxSum(nums1=[1, 4, 5, 8, 9, 11, 19], nums2=[2, 3, 4, 11, 12]))  # 61
