import itertools


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 分解质因子
        factors = [1]
        factor = 2
        temp = num
        while temp >= 0 and factor <= temp:
            if temp % factor == 0:
                factors.append(factor)
                temp //= factor
            else:
                factor += 1
            if temp == num  and factor > pow(num, 0.5) + 1:
                break

        print(factors)

        # 统计所有因子
        all_factors = [1] + factors
        for i in range(2, len(factors)):
            for group in itertools.combinations(factors, i):
                factor = 1
                for g in group:
                    factor *= g
                all_factors.append(factor)

        all_factors = set(all_factors)
        if num in all_factors:
            all_factors.remove(num)

        return sum(all_factors) == num


if __name__ == "__main__":
    print(Solution().checkPerfectNumber(28))  # True
    print(Solution().checkPerfectNumber(6))  # True
    print(Solution().checkPerfectNumber(496))  # True
    print(Solution().checkPerfectNumber(30402457))  # False
