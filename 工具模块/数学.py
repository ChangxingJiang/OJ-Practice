# 分解因子
def get_factor(x):
    factor = []
    now = 2
    while now <= x:
        while x % now == 0:
            factor.append(now)
            x //= now
        now += 1
    return factor


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
