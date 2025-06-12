def sieve(n):
    """质数筛"""

    # 创建一个布尔数组，初始都为 True（True 表示是质数）
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是质数

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # 将 i 的倍数全部标记为非质数
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # 返回所有为 True 的下标，即质数
    return {i for i, val in enumerate(is_prime) if val}


if __name__ == "__main__":
    # 样例：计算 10 万以内所有质数的集合
    prime_set = sieve(100000)
