from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().subdomainVisits(
        ["9001 discuss.leetcode.com"]))  # ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com",
                                      "5 wiki.org"]))  # ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
