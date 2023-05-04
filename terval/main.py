from time import time
from tabulate import tabulate

class T:
    def __init__(self, name="TERVAL", shut_up=False):
        self.name = name
        self.shut_up = shut_up
        self.last_time = time()
        self.all = []
        self.count = 1

    def __str__(self) -> str:
        return tabulate(self.all, tablefmt="fancy_grid")

    def x(self, name=""):
        now = time()
        elapsed = f"{(now - self.last_time):.5f} s"
        if not name:
            name = f"TASK {self.count}"
        if not self.shut_up:
            print(tabulate([[self.name, name, elapsed]], tablefmt="fancy_grid"))
        self.last_time = now
        self.count += 1
        self.all.append((name, elapsed))
    