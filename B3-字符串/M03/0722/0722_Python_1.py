from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    print(Solution().removeComments(
        source=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ",
                "   comment for ", "   testing */", "a = b + c;", "}"]))

    # ["ab"]
    print(Solution().removeComments(source=["a/*comment", "line", "more_comment*/b"]))
