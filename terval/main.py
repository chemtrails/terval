from time import time
from tabulate import tabulate
from typing import List


class T:
    def __init__(self, name: str = "TERVAL", silent: bool = False) -> None:
        self.name: str = name
        self.silent: bool = silent
        self.last_time: float = time()
        self.all: List = []
        self.count: int = 1

    def __str__(self) -> str:
        return tabulate(self.all, tablefmt="fancy_grid")

    def x(self, name: str = "") -> None:
        now: float = time()
        elapsed: str = f"{(now - self.last_time):.5f} s"
        if not name:
            name: str = f"TASK {self.count}"
        if not self.silent:
            print(tabulate([[self.name, name, elapsed]], tablefmt="fancy_grid"))
        self.last_time = now
        self.count += 1
        self.all.append((name, elapsed))

    @property
    def shut_up(self) -> None:
        self.silent = True
