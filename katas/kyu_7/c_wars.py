def initials(name):
    names = name.title().split()
    length = len(names) - 1
    return '.'.join(a[0] if length != i else a for i, a in enumerate(names))
