import filesystem as fs


c = 12345677


v = (c & (1 << 4)) >> 4

print(v)