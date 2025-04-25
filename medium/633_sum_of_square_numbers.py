import pytest


class Solution:
    def solve(self, c: int) -> bool:
        for a in range(int(c**0.5) + 1):
            square_b = c - a**2
            if (int(square_b**0.5))**2 == square_b:
                return True
        return False


@pytest.mark.parametrize("c, expected_value", [
    (1, True), (3, False), (5, True), (17, True), (19, False), (20, True), (24, False), (25, True)
])
def test_problem(c, expected_value):
    solution = Solution()
    ans = solution.solve(c)
    assert ans == expected_value
