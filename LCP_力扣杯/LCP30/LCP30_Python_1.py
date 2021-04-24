import heapq
from typing import List


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        room = []  # 当前扣血房间
        now = 1  # 当前血量

        if sum(nums) < 0:
            return -1

        ans = 0

        for num in nums:
            if num >= 0:  # 加血房间或不影响血量的房间
                now += num
            else:  # 扣血房间
                now += num
                heapq.heappush(room, num)
                while now <= 0 and room:  # 如果当前血量不是正值，则需要将之前扣血最多的房间移动到末尾（贪心）
                    now -= heapq.heappop(room)
                    ans += 1
                if now <= 0 and not room:  # 如果当前血量不是正值，且已经没有可以移动的房间，则说明无法通过
                    return -1

        return ans


if __name__ == "__main__":
    # 1
    print(Solution().magicTower(nums=[100, 100, 100, -250, -60, -140, -50, -50, 100, 150]))

    # -1
    print(Solution().magicTower(nums=[-200, -300, 400, 0]))

    # 自制用例：1
    print(Solution().magicTower(nums=[200, -200, -300, 300]))
