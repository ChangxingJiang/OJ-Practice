from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def check(val):
            # O(N)
            total = 0
            for i in inventory:
                if i > val:
                    total += i - val
            return total

        # O(N)
        left, right = 0, max(inventory)

        # 二分查找
        # O(NlogN)
        while left < right:
            mid = (left + right) // 2
            if check(mid) >= orders:
                left = mid + 1
            else:
                right = mid

        # 计算销售临界值
        sale_val = left

        # 计算销售临界值的总量(不卖临界值的情况下)
        sale_num = check(sale_val)

        # 计算临界值之上的结果
        ans = 0
        for i in inventory:
            if i > sale_val:
                ans += (sale_val + 1 + i) * (i - sale_val) // 2
                # print(i, "->", (sale_val + 1 + i) * (i - sale_val) // 2)

        # 计算临界值的结果
        ans += (orders - sale_num) * sale_val

        # print("临界值:", sale_val, sale_num)

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().maxProfit(inventory=[2, 5], orders=4))  # 14
    print(Solution().maxProfit(inventory=[3, 5], orders=6))  # 19
    print(Solution().maxProfit(inventory=[2, 8, 4, 10, 6], orders=20))  # 110
    print(Solution().maxProfit(inventory=[1000000000], orders=1000000000))  # 21
