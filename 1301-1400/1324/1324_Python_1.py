import itertools
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        return ["".join(elem).rstrip() for elem in itertools.zip_longest(*s.split(), fillvalue=" ")]


if __name__ == "__main__":
    print(Solution().printVertically(s="HOW ARE YOU"))  # ["HAY","ORO","WEU"]
    print(Solution().printVertically(s="TO BE OR NOT TO BE"))  # ["TBONTB","OEROOE","   T"]
    print(Solution().printVertically(s="CONTEST IS COMING"))  # ["CIC","OSO","N M","T I","E N","S G","T"]
