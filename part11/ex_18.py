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
        names = set(order.programmer for order in self.orders)
        return list(names)
    
    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f"no task with id {id}")
            
    def finished_orders(self):
        return [task for task in self.orders if task.finished]

    def unfinished_orders(self):     
        return [task for task in self.orders if not task.finished]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f"no programmer named {programmer}")
        
        finished = [task for task in self.finished_orders() if task.programmer == programmer]
        unfinished = [task for task in self.unfinished_orders() if task.programmer == programmer]

        return (len(finished), len(unfinished), sum(task.workload for task in finished), sum(task.workload for task in unfinished))
        
