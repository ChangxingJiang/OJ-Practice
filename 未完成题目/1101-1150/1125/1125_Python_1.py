from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        pass


if __name__ == "__main__":
    # [0,2]
    print(Solution().smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                                            people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))

    # [1,2]
    print(Solution().smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                            people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
                                                    ["java", "csharp", "aws"], ["reactjs", "csharp"],
                                                    ["csharp", "math"], ["aws", "java"]]))
