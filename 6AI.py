def vacuum(loc, a, b):
    c = 0
    if loc == 'A':
        if a == 'Dirty':
            a = 'Clean'; c += 1
        c += 1
        if b == 'Dirty':
            b = 'Clean'; c += 1
    else:
        if b == 'Dirty':
            b = 'Clean'; c += 1
        c += 1
        if a == 'Dirty':
            a = 'Clean'; c += 1
    print(f"A: {a}, B: {b}, Cost: {c}")

vacuum('A', 'Dirty', 'Dirty')
