from time import perf_counter_ns
from typing import Tuple
from tabulate import tabulate


class Terval:
    FG = "fancy_grid"
    def __init__(self, name: str = "TERVAL", silent: bool = False) -> None:
        t: int = perf_counter_ns()
        self.name: str = name
        self.silent: bool = silent
        self.prev_time: int = t
        self.first_time: int = t
        self.all: Tuple = ()
        self.count: int = 1

    def __str__(self) -> str:
        return tabulate(self.all + (("TOTAL", f"{(self.prev_time - self.first_time):_} ns"),), headers=(self.name, "performance"), tablefmt=self.FG)

    def x(self, name: str = "") -> None:
        elapsed: str = f"{((now := perf_counter_ns()) - self.prev_time):_} ns"
        if not name:
            name: str = f"TASK {self.count}"
        if not self.silent:
            print(tabulate(((self.name, name, elapsed),), tablefmt=self.FG))
        self.prev_time = now
        self.count += 1
        self.all += ((name, elapsed),)

    def toggle(self) -> None:
        self.silent = not self.silent
