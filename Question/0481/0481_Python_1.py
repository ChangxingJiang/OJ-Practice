class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        array = [1, 2, 2]
        i, now = 2, 1
        while len(array) < n:
            array.extend([now] * min(array[i], n - len(array)))
            i += 1
            now = 3 - now  # 1和2交换
        return array.count(1)


if __name__ == "__main__":
    print(Solution().magicalString(6))  # 3
    print(Solution().magicalString(0))  # 0
