import pytest
import math


class Solution:

    def solve(self, num: int) -> int:
        ans = 0
        while num > 0:
            if num <= 2:
                return ans + num
            if num & (num - 1) == 0:
                return ans + round(math.log2(num)) + 1
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            ans += 1
        return ans

    def solve2(self, num: int) -> int:
        action = {0: lambda x: x // 2, 1: lambda x: x - 1}
        ans = 0
        while num:
            num = action[num % 2](num)
            ans += 1
        return ans

    def test(self):
        test_cases = [
            [0, 0],
            [1, 1],
            [2, 2],
            [14, 6],
            [12, 5],
            [8, 4],
            [123, 12]
        ]
        for i, test_case in enumerate(test_cases):
            ans = self.solve2(test_case[0])
            correct_ans = test_case[-1]
            assert ans == correct_ans, f"Case {i} error, your answer is {ans}, but correct answer is {correct_ans}"
        print("All tests are successfully")


@pytest.mark.parametrize("num, expected_value", [
    (0, 0), (1, 1), (2, 2), (14, 6), (12, 5), (8, 4), (123, 12)
])
def test_problem(num, expected_value):
    solution = Solution()
    ans = solution.solve(num)
    assert ans == expected_value
