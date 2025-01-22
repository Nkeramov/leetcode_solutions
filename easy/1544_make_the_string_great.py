import pytest
from typing import List


class Solution:
    def solve(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


@pytest.mark.parametrize("input_list, expected_value", [
    ("leEeetcode", "leetcode"),
    ("abBAcC", ""),
    ("s", "s")
])
def test_problem(input_list, expected_value):
    solution = Solution()
    ans = solution.solve(input_list)
    assert ans == expected_value
