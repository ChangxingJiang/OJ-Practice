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


# 获取所有因子
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


# 已知每个值的分布数时计算中位数
def get_median(lst):
    vv = sum(lst)
    if len(lst) % 2 == 0:
        m1, m2 = vv // 2 - 1, vv // 2
        v1, v2 = -1, -1
        last = 0
        for i in range(len(lst)):
            last += lst[i]
            if last > m1 and v1 == -1:
                v1 = i
            if last > m2:
                v2 = i
                break
        return (v1 + v2) / 2
    else:
        m = vv // 2
        last = 0
        for i in range(len(lst)):
            last += lst[i]
            if last > m:
                return i
