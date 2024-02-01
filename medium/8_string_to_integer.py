import pytest


class Solution:
    def solve(self, s: str) -> int:
        s = s.strip()
        ans = 0
        if not s:
            return ans
        sign = -1 if s[0] == '-' else 1
        i = 1 if s[0] in '+-' else 0
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
        return max(-2**31, min(2**31 - 1, ans * sign))


@pytest.mark.parametrize("input_value, expected_value", [('42', 42), ('-42', -42), ('042', 42), ('    -42', -42),
                                                         ('4193 with words', 4193), ('words and 987', 0),
                                                         ('3.14159', 3)])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
