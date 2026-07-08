"""
Implementing @classmethod
"""

class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        return max(my_list, key=my_list.count)

    @classmethod
    def doubles(cls, my_list: list):
        unique_items = []
        for item in my_list:
            if item not in unique_items:
                unique_items.append(item)

        doubles = 0
        for item in unique_items:
            if my_list.count(item) >= 2:
                doubles += 1

        return doubles
