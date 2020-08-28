def drange(start, stop, step):
    r = start
    while r <= stop:
        yield r
        r += step


def decimal_generator(lower, higher, step):
    lower, higher = float(lower), float(higher)
    return [round(x, 2) for x in drange(lower, higher, step)]


if __name__ == '__main__':
    l = 2
    h = 5.5
    s = 0.5
    dg = decimal_generator(l, h, s)
    print(f"\nLiczby dziesiętne od {l} do {h} w kroku co {s} to:")
    for d in dg:
        print(f"{d}", end=", ")
    print()
    print()
