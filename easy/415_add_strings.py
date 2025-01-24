import pytest


class Solution:
    def solve(self, num1: str, num2: str) -> str:
        ans = []
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        carry = 0
        while i1 >= 0 or i2 >= 0 or carry:
            s = 0
            if i1 >= 0:
                s += int(num1[i1])
                i1 -= 1
            if i2 >= 0:
                s += int(num2[i2])
                i2 -= 1
            s += carry
            ans.append(str(s % 10))
            carry = s // 10
        return ''.join(ans[::-1])


@pytest.mark.parametrize("fist_string, second_string, expected_value", [
    ("11", "123", "134"),
    ("456", "77", "533"),
    ("1", "9", "10"),
    ("0", "0", "0")
])
def test_problem(fist_string, second_string, expected_value):
    solution = Solution()
    ans = solution.solve(fist_string, second_string)
    assert ans == expected_value
