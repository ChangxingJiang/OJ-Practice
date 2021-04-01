import collections
from math import factorial
from typing import List


# 分解因子
def get_factor(x):
    if x == 1:
        return [1]
    factor = []
    now = 2
    while now <= x:
        while x % now == 0:
            factor.append(now)
            x //= now
        now += 1
    return factor


class Solution:
    _MOD = 10 ** 9 + 7

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        return [self.count(n, k) for n, k in queries]

    def count(self, n, k):
        """计算方案数"""
        # 处理n为1的情况
        if n == 1:
            return 1

        # 处理k为1的情况
        if k == 1:
            return 1

        # ----- 下面处理n>1且k>1的情况 -----

        # 计算k的所有因子
        factors = get_factor(k)

        # 处理k只有1个质因子（自己）的情况
        if len(factors) == 1:
            return n

        # ----- 下面处理n>1且k>1且k不只1个质因子的情况 -----
        # 此时分别考虑每个质因子的分配方案数，再将各个质因子的分配方案数相乘
        # 相当于将l个小球（相同质因子的小球相同）放到n个不同的箱子中的方法
        # 使用重复组合公式
        res = 1

        factors_count = collections.Counter(factors)
        for factor, num in factors_count.items():
            res *= factorial(num + n - 1) // factorial(num) // factorial(n - 1)

        return int(res % self._MOD)


if __name__ == "__main__":
    # [4,1,50734910]
    print(Solution().waysToFillArray(queries=[[2, 6], [5, 1], [73, 660]]))

    # [1,2,3,10,5]
    print(Solution().waysToFillArray(queries=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))

    print(Solution().waysToFillArray(queries=[[403, 256]]))

    # 测试用例 52/67
    # print(Solution().waysToFillArray(queries=
    #                                  [[326, 476], [160, 348], [476, 238], [33, 194], [306, 54], [138, 500], [486, 320],
    #                                   [92, 28], [372, 216], [5, 214], [125, 334], [190, 96], [327, 500], [403, 435],
    #                                   [232, 119], [70, 226], [171, 118], [63, 192], [437, 417], [221, 447], [236, 422],
    #                                   [368, 414], [326, 329], [257, 330], [207, 308], [305, 13], [21, 430], [371, 79],
    #                                   [143, 39], [154, 186], [33, 362], [494, 55], [225, 72], [18, 323], [369, 244],
    #                                   [308, 408], [352, 419], [155, 67], [34, 113], [151, 384], [473, 289], [272, 376],
    #                                   [391, 360], [443, 344], [23, 460], [350, 446], [441, 331], [116, 70], [143, 270],
    #                                   [470, 259], [483, 224], [274, 215], [445, 183], [456, 7], [403, 256], [42, 451],
    #                                   [316, 492], [182, 319], [378, 471], [54, 475], [4, 315], [356, 136], [336, 97],
    #                                   [332, 461], [54, 324], [337, 112], [458, 126], [441, 218], [278, 391], [377, 179],
    #                                   [198, 456], [62, 481], [262, 404], [208, 234], [352, 52], [402, 213], [254, 385],
    #                                   [311, 111], [437, 190], [156, 173], [296, 401], [5, 162], [100, 290], [354, 140],
    #                                   [160, 484], [376, 104], [443, 429], [103, 201], [346, 374], [371, 483],
    #                                   [270, 51]]))
