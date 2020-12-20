# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:
        result = 0
        for i in range(n):
            # 如果result认识其他任何一个人，则说明result不是名人
            if knows(result, i):
                result = i

        for i in range(n):
            if result != i and (knows(result, i) or not knows(i, result)):
                return -1

        return result


if __name__ == "__main__":
    pass
