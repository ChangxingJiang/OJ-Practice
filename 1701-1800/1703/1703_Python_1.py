from typing import List


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # 统计各个1之间的距离
        lst1 = []
        now = -1
        for num in nums:
            if num == 1:
                if now != -1:
                    lst1.append(now)
                now = 0
            else:
                if now != -1:
                    now += 1

        # 处理k==2的特殊情况
        if k == 2:
            return min(lst1)

        # 构造每一小段的列表
        # [1,2(2次),3(3次),4] = [1,2] + [2,3] + [3,4]
        size = k // 2
        times = (k + 1) // 2
        now = sum(lst1[:size])
        lst2 = [now]
        for i in range(len(lst1) - size):
            now = now - lst1[i] + lst1[i + size]
            lst2.append(now)

        # 滑动窗口
        ans = now = sum(lst2[:times])
        for i in range(len(lst2) - times):
            now = now - lst2[i] + lst2[i + times]
            ans = min(ans, now)

        return ans


if __name__ == "__main__":
    print(Solution().minMoves(nums=[1, 0, 0, 1, 0, 1], k=2))  # 1
    print(Solution().minMoves(nums=[1, 0, 0, 0, 0, 0, 1, 1], k=3))  # 5
    print(Solution().minMoves(nums=[1, 1, 0, 1], k=2))  # 0

    # 自制用例
    print(Solution().minMoves(nums=[1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], k=5))  # 15
