import collections
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            for file in path[1:]:
                file = file.split("(")
                content = file[1].replace(")", "")
                hashmap[content].append(folder + "/" + file[0])

        ans = []
        for key, value in hashmap.items():
            if len(value) >= 2:
                ans.append(value)

        return ans


if __name__ == "__main__":
    # [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
