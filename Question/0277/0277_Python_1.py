# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            for j in range(n):
                if i != j and (not knows(j, i) or knows(i, j)):
                    break
            else:
                return i
        return -1


if __name__ == "__main__":
    pass
