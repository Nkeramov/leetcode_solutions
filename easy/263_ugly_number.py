import pytest


class Solution:
    def solve(self, n: int) -> bool:
        if n <= 0:
            return False
        for primes in 2, 3, 5:
            while n % primes == 0:
                n //= primes
        return n == 1


@pytest.mark.parametrize("x, expected_value", [(1, True), (14, False), (6, True), (7, False)])
def test_problem(x, expected_value):
    solution = Solution()
    ans = solution.solve(x)
    assert ans == expected_value
