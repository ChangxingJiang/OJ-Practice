from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    # [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
