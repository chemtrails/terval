from time import perf_counter_ns
from tabulate import tabulate


class Perf:
    def __init__(self, silent: bool = False) -> None:
        self.prev_time = perf_counter_ns()
        self.count = 1
        self.sum = 0
        self.all = ()
        self.silent = silent

    def __str__(self) -> str:
        return tabulate(self.all + (("TOTAL", f"{(self.sum):_}"),), headers=("TASK", "PERFORMANCE (ns)"), tablefmt="fancy_grid")

    def x(self, name: str = "") -> None:
        t = perf_counter_ns()
        elapsed = t - self.prev_time
        self.all += ((name or f"task {self.count}", f"{(elapsed):_}"),)
        if self.silent is False:
            print(tabulate(((name or f"task {self.count}", f"{(elapsed):_}"),), tablefmt="fancy_grid"))
        self.sum += elapsed
        self.count += 1
        self.prev_time = perf_counter_ns()
