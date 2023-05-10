Terval simply prints the time elapsed since it was last called in nanoseconds

```
pip install git+https://github.com/chemtrails/terval
```

```py
from time import sleep
from terval import Terval

timer = Terval("timer", silent=True)

sleep(0.1)
timer.x("named task")

for _ in range(2):
    sleep(0.1)
    timer.x()

print(timer)
```

![image](https://raw.githubusercontent.com/chemtrails/terval/master/images/terminal.png)

silent is False by default. Call `toggle()` to stop or resume printing

```py
timer = Terval()

sleep(0.1)
timer.x()

timer.toggle()

sleep(0.1)
timer.x()

timer.toggle()

sleep(0.1)
timer.x()
```

![image](https://raw.githubusercontent.com/chemtrails/terval/master/images/terminal2.png)

Dependencies:
- tabulate
