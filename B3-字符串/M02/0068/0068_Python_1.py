from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        pass


if __name__ == "__main__":
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]
    print(Solution().fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))

    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]
    print(Solution().fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
