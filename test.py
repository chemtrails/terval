import time
import terval


def sleep(t):
    time.sleep(t)


t = terval.T("timer", shut_up=True)

sleep(0.002)
t.x()

sleep(0.1)
t.x("some task")

sleep(0.3)
t.x()

sleep(0.11)
t.x()

print(t)
