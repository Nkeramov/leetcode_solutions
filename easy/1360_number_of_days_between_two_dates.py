import pytest


class Solution:

    def is_leap_year(self, year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_days_in_month(self, month: int, year: int) -> int:
        if 0 < month < 13:
            mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return mdays[month - 1] + (month == 2 and self.is_leap_year(year))
        return 0

    def get_days_in_year(self, year: int) -> int:
        return 365 + self.is_leap_year(year)

    def solve(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1
        y1, m1, d1 = [int(x) for x in date1.split('-')]
        y2, m2, d2 = [int(x) for x in date2.split('-')]
        if y1 == y2:
            if m1 == m2:
                return d2 - d1
            else:
                ans = self.get_days_in_month(m1, y1) - d1
                if m2 - m1 > 1:
                    for m in range(m1 + 1, m2):
                        ans += self.get_days_in_month(m, y1)
                ans += d2
                return ans
        else:
            ans = self.get_days_in_month(m1, y1) - d1
            if m1 < 12:
                for m in range(m1 + 1, 13):
                    ans += self.get_days_in_month(m, y1)
            if y2 - y1 > 1:
                for y in range(y1 + 1, y2):
                    ans += self.get_days_in_year(y)
            if m2 > 1:
                for m in range(1, m2):
                    ans += self.get_days_in_month(m, y2)
            ans += d2
            return ans


@pytest.mark.parametrize("first_date, second_date, expected_value", [
    ('2021-07-10', '2021-07-10', 0),
    ('2019-06-29', '2019-06-30', 1),
    ('2013-09-23', '2013-04-14', 162),
    ('2020-01-15', '2019-12-31', 15),
    ('1980-01-06', '2001-09-01', 7909)
])
def test_problem(first_date, second_date, expected_value):
    solution = Solution()
    ans = solution.solve(first_date, second_date)
    assert ans == expected_value
