from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["tree", "used"]
    print(Solution().getValidT9Words(num="8733", words=["tree", "used"]))

    # ["a", "b", "c"]
    print(Solution().getValidT9Words(num="2", words=["a", "b", "c", "d"]))
