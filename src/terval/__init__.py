from time import perf_counter_ns
from tabulate import tabulate


class Terval:
    def __init__(self, name: str = "TERVAL", silent: bool = False) -> None:
        self.prev_time = self.first_time = perf_counter_ns()
        self.name = name
        self.silent = silent
        self.count = 1
        self.all = ()

    def __str__(self) -> str:
        return tabulate(self.all + (("TOTAL", f"{(self.prev_time - self.first_time):_} ns"),), headers=(self.name, "PERFORMANCE"), tablefmt="fancy_grid")

    def x(self, name: str = "") -> None:
        elapsed = f"{((t := perf_counter_ns()) - self.prev_time):_} ns"
        if not name:
            name = f"TASK {self.count}"
        if not self.silent:
            print(tabulate(((self.name, name, elapsed),), tablefmt="fancy_grid"))
        self.prev_time = t
        self.count += 1
        self.all += ((name, elapsed),)

    def toggle(self) -> None:
        self.silent = not self.silent
