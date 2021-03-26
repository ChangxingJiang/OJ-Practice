import collections
from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        i1, i2, i3 = 0, 0, 0  # 有K个不同的数组的开头，有K-1个不同的数组的开头，两个数组的结尾
        count1, count2 = collections.Counter(), collections.Counter()  # i1到i3的数组的情况，i2到i3的数组的情况

        ans = 0

        size = len(A)
        while i3 < size:
            # 移动数组右侧边缘指针
            ch3 = A[i3]
            count1[ch3] += 1
            count2[ch3] += 1

            # 移动i1到i3的数组左侧边缘指针
            while i1 <= i3 and len(count1) > K:
                ch1 = A[i1]
                count1[ch1] -= 1
                if count1[ch1] == 0:
                    del count1[ch1]
                i1 += 1

            # 移动i2到i3的数组左侧边缘指针
            while i2 <= i3 and len(count2) > K - 1:
                ch2 = A[i2]
                count2[ch2] -= 1
                if count2[ch2] == 0:
                    del count2[ch2]
                i2 += 1

            # 累加结果
            if len(count1) == K and len(count2) == K - 1:
                ans += i2 - i1

            i3 += 1

        return ans


if __name__ == "__main__":
    print(Solution().subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=2))  # 7
    print(Solution().subarraysWithKDistinct(A=[1, 2, 1, 3, 4], K=3))  # 3
    print(Solution().subarraysWithKDistinct(A=[1, 2], K=1))  # 2
