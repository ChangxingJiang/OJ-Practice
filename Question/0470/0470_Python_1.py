import random


# The rand7() API is already defined for you.
def rand7():
    return random.randint(1, 7)


# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        idx = 50
        while idx >= 40:
            i1, i2 = rand7(), rand7()
            idx = (i1 - 1) * 7 + i2 - 1
        return idx % 10 + 1


if __name__ == "__main__":
    print(Solution().rand10())  # [7]
    print(Solution().rand10())  # [8,4]
    print(Solution().rand10())  # [8,1,10]
