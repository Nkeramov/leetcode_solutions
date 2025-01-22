import pytest
from typing import List


class Solution:
    def solve(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if not ans or ans and abs(ord(s[i]) - ord(ans[-1])) != 32:
                ans += s[i]
            else:
                ans = ans[:-1]
        return ans


@pytest.mark.parametrize("input_list, expected_value", [
    ("leEeetcode", "leetcode"),
    ("abBAcC", ""),
    ("s", "s"),
    ("hHcOzoC", "cOzoC")
])
def test_problem(input_list, expected_value):
    solution = Solution()
    ans = solution.solve(input_list)
    assert ans == expected_value
