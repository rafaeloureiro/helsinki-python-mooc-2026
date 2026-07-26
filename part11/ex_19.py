"""

"""

class Task:
    next_id = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.next_id
        Task.next_id += 1

    def is_finished(self) -> bool:
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.orders.append(task)

    def all_orders(self) -> list:
        return self.orders

    def programmers(self) -> list:
        return list(set(order.programmer for order in self.orders))

    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f"no task with id {id}")

    def finished_orders(self) -> list:
        return [task for task in self.orders if task.finished]

    def unfinished_orders(self) -> list:
        return [task for task in self.orders if not task.finished]

    def status_of_programmer(self, programmer: str) -> tuple:
        if programmer not in self.programmers():
            raise ValueError(f"no programmer named {programmer}")
        finished = [t for t in self.finished_orders() if t.programmer == programmer]
        unfinished = [t for t in self.unfinished_orders() if t.programmer == programmer]
        return (
            len(finished),
            len(unfinished),
            sum(t.workload for t in finished),
            sum(t.workload for t in unfinished),
        )


def print_menu():
    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")


def main():
    orders = OrderBook()
    print_menu()

    while True:
        command = input("command: ")

        if command == "0":
            break

        elif command == "1":
            description = input("description: ")
            details = input("programmer and workload estimate: ")
            parts = details.split()
            if len(parts) != 2 or not parts[1].isdigit():
                print("erroneous input")
                continue
            programmer, workload = parts[0], int(parts[1])
            orders.add_order(description, programmer, workload)
            print("added!")

        elif command == "2":
            finished = orders.finished_orders()
            if len(finished) == 0:
                print("no finished tasks")
            else:
                for task in finished:
                    print(task)

        elif command == "3":
            unfinished = orders.unfinished_orders()
            if len(unfinished) == 0:
                print("no unfinished tasks")
            else:
                for task in unfinished:
                    print(task)

        elif command == "4":
            id_input = input("id: ")
            if not id_input.isdigit():
                print("erroneous input")
                continue
            try:
                orders.mark_finished(int(id_input))
                print("marked as finished")
            except ValueError:
                print("erroneous input")

        elif command == "5":
            for programmer in orders.programmers():
                print(programmer)

        elif command == "6":
            programmer = input("programmer: ")
            try:
                finished, unfinished, done, scheduled = orders.status_of_programmer(programmer)
                print(f"tasks: finished {finished} not finished {unfinished}, hours: done {done} scheduled {scheduled}")
            except ValueError:
                print("erroneous input")

        else:
            print("erroneous input")

main()
