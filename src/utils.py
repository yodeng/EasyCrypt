class UsageError(Exception):
    pass


def add_to_16(v):
    while len(v) % 16 != 0:
        v = v + "\0"
    # @@
    return v
