class Solution:
    _BIG = 10 ** 9

    def reorderedPowerOf2(self, N: int) -> bool:
        aim = set()

        now = 1
        while now < min(self._BIG, N * 10):
            lst = [0] * 10
            for ch in str(now):
                lst[int(ch)] += 1
            aim.add(tuple(lst))
            now *= 2

        lst = [0] * 10
        for ch in str(N):
            lst[int(ch)] += 1
        return tuple(lst) in aim


if __name__ == "__main__":
    print(Solution().reorderedPowerOf2(1))  # True
    print(Solution().reorderedPowerOf2(10))  # False
    print(Solution().reorderedPowerOf2(16))  # True
    print(Solution().reorderedPowerOf2(24))  # False
    print(Solution().reorderedPowerOf2(46))  # True
