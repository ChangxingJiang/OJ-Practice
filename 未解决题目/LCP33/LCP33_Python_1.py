import math
from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        size = len(bucket)

        ans1 = 0

        # 处理水桶为0且水缸不为0的情况
        for i in range(size):
            if bucket[i] == 0 and vat[i] != 0:
                bucket[i] += 1
                ans1 += 1

        # 计算极限最大次数
        max_lst = [math.ceil(vat[i] / bucket[i]) if bucket[i] > 0 else 0 for i in range(size)]
        maximum = max(max_lst)
        # print("极限最大次数:", maximum)

        if maximum == 0:
            return 1

        # 定义状态矩阵
        dp = [[0] * size for _ in range(maximum + 1)]  # 第i个桶需要倒j次水所需要的增加容积次数

        # 计算所有状态
        # 最大时间复杂度:100 * 10000
        for i in range(size):  # 遍历坐标
            for j in range(max_lst[i], 0, -1):  # 遍历倒水次数
                dp[j][i] = math.ceil(vat[i] / j) - min(bucket[i], vat[i])

        # for row in dp:
        #     print(row)

        # 计算最终结果
        ans2 = 1000000
        for j in range(1, maximum + 1):
            ans2 = min(ans2, j + sum(dp[j]))

        return ans1 + ans2


if __name__ == "__main__":
    print(Solution().storeWater(bucket=[1, 3], vat=[6, 8]))  # 4
    print(Solution().storeWater(bucket=[9, 0, 1], vat=[0, 2, 2]))  # 3

    # 自制测试用例
    print(Solution().storeWater(bucket=[1, 5, 3, 3, 5], vat=[2, 14, 6, 6, 10]))  # 3
    print(Solution().storeWater(bucket=[2, 0, 1], vat=[8, 2, 2]))  # 5
    print(Solution().storeWater(bucket=[2, 1, 1], vat=[8, 0, 2]))  # 4
    print(Solution().storeWater(bucket=[2], vat=[1]))  # 1
    print(Solution().storeWater(bucket=[2], vat=[0]))  # 1
    print(Solution().storeWater(bucket=[2], vat=[10000]))  # 198
