"""
Class money with few overload operators.
"""

class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return (f"{self.__euros}.0{self.__cents} eur")
        elif self.__cents >= 10:    
            return (f"{self.__euros}.{self.__cents} eur")      

    def _to_cents(self):
        return self.__euros * 100 + self.__cents

    def __eq__(self, another):
        return self._to_cents() == another._to_cents()

    def __ne__(self, another):
        return self._to_cents() != another._to_cents()

    def __lt__(self, another):
        return self._to_cents() < another._to_cents()

    def __gt__(self, another):
        return self._to_cents() > another._to_cents()

    def __add__(self, another):
        total_cents = self._to_cents() + another._to_cents()
        return Money(total_cents // 100, total_cents % 100)

    def __sub__(self, another):
        total_cents = self._to_cents() - another._to_cents()
        if total_cents < 0:
            raise ValueError("a negative result is not allowed")
        return Money(total_cents // 100, total_cents % 100)
