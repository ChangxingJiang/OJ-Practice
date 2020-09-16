from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def helper(t):
            r3 = t % 3
            r5 = t % 5
            if r3 == 0 and r5 == 0:
                return "FizzBuzz"
            elif r3 == 0:
                return "Fizz"
            elif r5 == 0:
                return "Buzz"
            else:
                return str(t)

        return [helper(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    print(Solution().fizzBuzz(15))
    # [
    #     "1",
    #     "2",
    #     "Fizz",
    #     "4",
    #     "Buzz",
    #     "Fizz",
    #     "7",
    #     "8",
    #     "Fizz",
    #     "Buzz",
    #     "11",
    #     "Fizz",
    #     "13",
    #     "14",
    #     "FizzBuzz"
    # ]
