"""
Overload operators within class SimpleDate.

For simplicity's is assumed that each month has 30 days.
"""

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __ne__(self, other):
        return (self.year, self.month, self.day) != (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)
    
    def __add__(self, days: int):
        total_days = self.year * 360 + (self.month - 1) * 30 + (self.day - 1)
        total_days += days

        new_day = total_days % 30 + 1
        remaining_months = total_days // 30
        new_month = remaining_months % 12 + 1
        new_year = remaining_months // 12

        return SimpleDate(new_day, new_month, new_year)
    
    def __sub__(self, other):
        self_days = self.year * 360 + (self.month - 1) * 30 + (self.day - 1)
        other_days = other.year * 360 + (other.month - 1) * 30 + (other.day - 1)
        dif_days = abs(self_days - other_days)

        return dif_days
