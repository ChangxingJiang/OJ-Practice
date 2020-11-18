from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 计算前缀和
        # O(N)
        prefix = [0]
        last = 0
        for num in nums:
            last += num
            prefix.append(last)

        print(prefix)

        # 归并排序计算前缀和对
        # O(NlogN)
        def count(pp, left, right):
            # 处理递归结束的情况
            if left == right:
                return 0
            else:
                mid = (left + right) // 2

                # 递归归并排序左右两部分的数组，并计算两部分的数组中的答案数量
                ans = count(pp, left, mid) + count(pp, mid + 1, right)

                # 计算当前左右两部分各1个的答案数量
                # 滑动窗口
                i1, i2, i3 = left, mid + 1, mid + 1  # 左侧数组坐标，右侧数组滑动窗口左右边界
                while i1 <= mid:
                    while i2 <= right and pp[i2] - pp[i1] < lower:
                        i2 += 1
                    while i3 <= right and pp[i3] - pp[i1] <= upper:
                        i3 += 1
                    ans += i3 - i2
                    i1 += 1

                # 归并排序合并两个排序数组
                result = []
                i1, i2 = left, mid + 1
                while i1 <= mid and i2 <= right:
                    if pp[i1] <= pp[i2]:
                        result.append(pp[i1])
                        i1 += 1
                    else:
                        result.append(pp[i2])
                        i2 += 1
                while i1 <= mid:
                    result.append(pp[i1])
                    i1 += 1
                while i2 <= right:
                    result.append(pp[i2])
                    i2 += 1

                for i in range(len(result)):
                    pp[i + left] = result[i]

                return ans

        return count(prefix, 0, len(prefix) - 1)


if __name__ == "__main__":
    print(Solution().countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))  # 3
