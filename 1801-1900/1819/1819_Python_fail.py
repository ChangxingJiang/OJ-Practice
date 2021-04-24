import collections
import math
from typing import List


# 求n以下的质数
def get_primes(n: int) -> list:
    if n < 2:
        return [1]

    num_list = [True] * n
    num_list[0], num_list[1] = False, False

    for i in range(2, int(pow(n, 0.5)) + 1):
        if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
            num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

    return [i for i in range(n) if num_list[i]]


# 分解质因子（小于等于200000）
primes = get_primes(450)
# print(len(primes), primes)


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


# 枚举所有可能的组合
def enumeration(factor):
    count = collections.Counter(factor)
    lst = list(count.keys())
    size = len(lst)

    ans = set()

    def dfs(i, now):
        if i == size:
            ans.add(now)
        else:
            for j in range(count[lst[i]] + 1):
                dfs(i + 1, now * (lst[i] ** j))

    dfs(0, 1)

    return list(sorted(ans))


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        waiting = collections.defaultdict(set)
        ans = set(nums)

        for num in nums:
            factor = get_prime_factors(num)
            all_factor = enumeration(factor)
            # print(num, factor, all_factor)

            for i in range(len(all_factor)):
                f1, f2 = all_factor[i], all_factor[-i - 1]
                if all_factor[i] not in ans:
                    for f3 in waiting[f1]:
                        if math.gcd(f3, f2) == 1:
                            ans.add(f1)
                            break
                    else:
                        waiting[f1].add(f2)

        return len(ans)


if __name__ == "__main__":
    print(Solution().countDifferentSubsequenceGCDs(nums=[6, 10, 3]))  # 5
    print(Solution().countDifferentSubsequenceGCDs(nums=[5, 15, 40, 5, 6]))  # 7
