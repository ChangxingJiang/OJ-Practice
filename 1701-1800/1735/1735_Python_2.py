import collections
from math import comb
from typing import List

_MOD = 10 ** 9 + 7


# 求n以下的质数
def get_primes(n: int) -> list:
    if n < 2:
        return []

    num_list = [True] * n
    num_list[0], num_list[1] = False, False

    for i in range(2, int(pow(n, 0.5)) + 1):
        if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
            num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

    return [i for i in range(n) if num_list[i]]


# 分解质因子（小于等于10000）
primes = get_primes(101)


def get_prime_factors(x):
    res = []
    for prime in primes:
        if prime > x:
            break
        while x % prime == 0:
            res.append(prime)
            x //= prime

    if x > 1:
        res.append(x)

    return res


class Solution:
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
        factors = get_prime_factors(k)

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
            res *= comb(num + n - 1, n - 1)  # 最多乘num个，num≤14

        return res % _MOD


if __name__ == "__main__":
    # [4,1,50734910]
    print(Solution().waysToFillArray(queries=[[2, 6], [5, 1], [73, 660]]))

    # [1,2,3,10,5]
    print(Solution().waysToFillArray(queries=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))

    # 测试用例 28/67 : [865201973,101,466,308,411805778]
    print(Solution().waysToFillArray([[373, 196], [101, 229], [466, 109], [308, 83], [296, 432]]))

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
