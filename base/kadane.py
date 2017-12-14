def kadane(lst):
    max_current = max_global = lst[0]
    for i in range(len(lst) -1):
        max_current = max([lst[i], max_current + lst[i]])
        if max_current > max_global:
            max_global = max_current

    return max_global


if __name__ == '__main__':
    p = kadane([1,2,3,21,1,2])
    print 'p -->', p
