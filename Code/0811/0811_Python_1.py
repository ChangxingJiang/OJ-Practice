from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for cpdomain in cpdomains:
            cp_split = cpdomain.split(" ")
            num = int(cp_split[0])
            domain = cp_split[1]
            while len(domain) > 0:
                if domain not in hashmap:
                    hashmap[domain] = num
                else:
                    hashmap[domain] += num
                if "." not in domain:
                    break
                else:
                    domain = domain[domain.index(".") + 1:]

        ans = []
        for key, value in hashmap.items():
            ans.append(str(value) + " " + key)
        return ans


if __name__ == "__main__":
    print(Solution().subdomainVisits(
        ["9001 discuss.leetcode.com"]))  # ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com",
                                      "5 wiki.org"]))  # ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
