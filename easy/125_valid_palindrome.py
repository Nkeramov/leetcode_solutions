import pytest
from typing import List


class Solution:
    def solve(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        left, right = 0, len(s)-1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            elif s[left].isalnum():
                right -= 1
            else:
                left += 1
        return True


@pytest.mark.parametrize("input_list, expected_value", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True)
])
def test_problem(input_list, expected_value):
    solution = Solution()
    ans = solution.solve(input_list)
    assert ans == expected_value
