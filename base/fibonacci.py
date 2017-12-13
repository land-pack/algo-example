def fab(n):
    if n in (0, 1, 2):
        return n

    return fab(n-1) + fab(n -2)

if __name__ == '__main__':
    for i in range(10):
        print fab(i)
