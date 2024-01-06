import pytest


class Solution:
    def solve(self, x: int) -> bool:
        return x >= 0 and (x < 10 or x == int(str(x)[::-1]))

    def solve2(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


@pytest.mark.parametrize("input_value, expected_value", [(121, True), (-121, False), (10, False), (11, True)])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
