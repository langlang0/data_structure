import time


def f(num: int):
    if num <= 1:
        return num
    else:
        return f(num - 1) + f(num - 2)


start = time.time()
print(f(40))
end = time.time()
dur = end - start
print(dur)
