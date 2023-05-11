### Terval measures, formats and prints performance

```console
pip install git+https://github.com/chemtrails/terval
```

Fake function:

```py
import time
def fake():
    time.sleep(0.1)
```

### Example of a default timer

Call `x()` after every task

Call `toggle()` to stop and resume printing

```py
from terval import Terval

timer = Terval()

fake()
timer.x()

# stop printing
timer.toggle()

fake()
# this will not be printed
timer.x()

# resume printing
timer.toggle()

fake()
timer.x()
```

![image](https://raw.githubusercontent.com/chemtrails/terval/master/images/terminal2.png)

### Example of a silent timer and named task

`print(timer)` to show summary

```py
timer = Terval("timer", silent=True)

fake()
timer.x("named task")

for _ in range(2):
    fake()
    timer.x()

print(timer)
```

![image](https://raw.githubusercontent.com/chemtrails/terval/master/images/terminal.png)

### Dependencies
- tabulate
