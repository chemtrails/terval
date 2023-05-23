#### Terval - Performance counter

```bash
pip install git+https://github.com/chemtrails/terval.git
```

Usage
```py
from terval import Perf

perf = Perf()

do_something()
perf.x("Something")

do_something_else()    
perf.x("Something else")
```

Turn printing off
```py
perf.silent = True
```

Show summary
```py
print(perf)
```
