import pytest


class Solution:
    def solve(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11
        if len(str(n)) % 2 == 0:
            limit = pow(10, len(str(n)) // 2)
        else:
            limit = str(n)[:len(str(n)) // 2 + 1]
        for i in range(int(limit), 20000):
            x = int(str(i) + str(i)[:-1][::-1])
            if x >= n and self.is_prime(x):
                return x

    def is_prime(self, n: int) -> bool:
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5) + 1
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True


@pytest.mark.parametrize("input_value, expected_value", [
    (6, 7), (8, 11), (13, 101), (9989900, 100030001)
])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value


