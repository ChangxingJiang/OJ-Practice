class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = 1
        cnt = 0
        while cnt < n:
            tmp = num
            while tmp % 2 == 0:
                tmp /= 2
            while tmp % 3 == 0:
                tmp /= 3
            while tmp % 5 == 0:
                tmp /= 5
            if tmp == 1:
                cnt += 1
                if cnt == n:
                    return num
            num += 1


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))  # 12
