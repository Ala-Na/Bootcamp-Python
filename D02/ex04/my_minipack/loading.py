import time
from time import sleep

def ft_progress(lst):
    start = time.time()
    eta = 0
    arrow = ">"
    for i in lst:
        elaps_time = time.time() - start
        if i != 0:
            eta = elaps_time * ((len(lst) - (i + 1)) / (i + 1))
        percent = ((i + 1) * 100) / len(lst)
        bar_size = percent / 5
        while (len(arrow) < bar_size + 1):
            arrow = "=" + arrow
        print("\rETA: {: 6.2f}s [{:5.1f}%][{:21}] {: 5}/{} | elapsed time {: 6.2f}s".format(eta, percent, arrow, i + 1, len(lst), elaps_time), end="", flush=True)
        yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret, "\n")

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)