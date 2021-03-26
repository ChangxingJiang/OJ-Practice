from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        size = len(nums)

        # 处理开口向上的情况
        if a > 0:
            # 计算对称轴的x坐标
            mid = -(b / (2 * a))

            ans = []
            l, r = 0, size - 1
            while l <= r:
                if abs(mid - nums[l]) >= abs(nums[r] - mid):
                    v = nums[l]
                    l += 1
                else:
                    v = nums[r]
                    r -= 1
                ans.append(a * v * v + b * v + c)
            ans.reverse()
            return ans

        # 处理开口向下的情况
        elif a < 0:
            # 计算对称轴的x坐标
            mid = -(b / (2 * a))

            ans = []
            l, r = 0, size - 1
            while l <= r:
                if abs(mid - nums[l]) >= abs(nums[r] - mid):
                    v = nums[l]
                    l += 1
                else:
                    v = nums[r]
                    r -= 1
                ans.append(a * v * v + b * v + c)
            return ans

        # 处理一次函数的情况
        else:
            ans = []
            for i in range(size):
                ans.append(b * nums[i] + c)
            # 处理单调递减的情况
            if b < 0:
                ans.reverse()
            return ans


if __name__ == "__main__":
    #  [3,9,15,33]
    print(Solution().sortTransformedArray(nums=[-4, -2, 2, 4], a=1, b=3, c=5))

    # [-23,-5,1,7]
    print(Solution().sortTransformedArray(nums=[-4, -2, 2, 4], a=-1, b=3, c=5))
