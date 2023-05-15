### Terval measures, formats and prints performance

```console
pip install git+https://github.com/chemtrails/terval.git
```

### Example

```py
from time import sleep
from terval import Terval

t = Terval()

sleep(0.1)
t.x("named task")

for _ in range(2):
    sleep(0.1)
    t.x()

print(timer)
```

![image](https://raw.githubusercontent.com/chemtrails/terval/master/images/terminal.png)
