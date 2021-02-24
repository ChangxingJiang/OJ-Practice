fibonacci_list = [1, 1]
while fibonacci_list[-2] + fibonacci_list[-1] <= 10 ** 9:
    fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ans = 0
        for num in fibonacci_list[::-1]:
            if k >= num:
                ans += 1
                k -= num
        return ans


if __name__ == "__main__":
    print(Solution().findMinFibonacciNumbers(7))  # 2
    print(Solution().findMinFibonacciNumbers(10))  # 2
    print(Solution().findMinFibonacciNumbers(19))  # 3
