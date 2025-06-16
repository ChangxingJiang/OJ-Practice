import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


class Solution:

    def sumOfLargestPrimes(self, s: str) -> int:
        n = len(s)
        value_set = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                ss = s[i:j]
                if is_prime(int(ss)):
                    value_set.add(int(ss))
        value_list = sorted(value_set, reverse=True)
        if len(value_list) <= 3:
            return sum(value_list)
        return sum(value_list[:3])


if __name__ == "__main__":
    print(Solution().sumOfLargestPrimes("12234"))  # 1469
    print(Solution().sumOfLargestPrimes("111"))  # 11
