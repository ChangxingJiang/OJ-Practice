from typing import List


# 滑动窗口
# O(N^2)

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # 符合条件的数组
        ans_list = []

        # 滑动窗口需要符合条件的数组
        # O(N)
        size = len(arr)
        left, right = 0, 0  # 滑动窗口的左右边界
        window = 0  # 滑动窗口中的和
        while right <= size:
            # 滑动窗口
            if window < target:
                if right < size:
                    window += arr[right]
                    right += 1
                else:
                    break
            else:
                window -= arr[left]
                left += 1

            # 判断窗口值是否符合要求
            if window == target:
                ans_list.append((right - left, left, right - 1))

        # 处理没有符合的要求的情况
        if len(ans_list) < 2:
            return -1

        # 排序所有符合要求的窗口值（窗口宽度 -> 窗口左侧边框）
        # O(NlogN)
        ans_list.sort()

        # print(ans_list)

        # 遍历窗口寻找结果
        # O(N^2)
        ans = float("inf")
        for i in range(len(ans_list)):
            first = ans_list[i]  # 第1个窗口的宽度
            if first[0] >= ans:
                break

            for j in range(i + 1, len(ans_list)):
                second = ans_list[j]
                if first[0] + second[0] >= ans:
                    break

                # 处理存在重叠的情况
                if first[1] <= second[1] <= first[2] or first[1] <= second[2] <= first[2]:
                    continue

                ans = min(ans, first[0] + second[0])

        return ans if ans <= size else -1


if __name__ == "__main__":
    print(Solution().minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3))  # 2
    print(Solution().minSumOfLengths(arr=[7, 3, 4, 7], target=7))  # 2
    print(Solution().minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6))  # -1
    print(Solution().minSumOfLengths(arr=[5, 5, 4, 4, 5], target=3))  # -1
    print(Solution().minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3))  # 3
    print(Solution().minSumOfLengths(arr=[1, 1, 1, 2, 2, 2, 4, 4], target=6))  # 6

    print(Solution().minSumOfLengths(
        arr=[2, 2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=20))  # 23

    print(Solution().minSumOfLengths(arr=[1, 6, 1], target=7))  # -1
