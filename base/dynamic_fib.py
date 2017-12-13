def fib(n):
    # assuming n > 2
    seq = range(n)
    seq[0]=seq[1]=1 # init 
    for i in seq[2:]:
        seq[i] = seq[i-1] + seq[i-2]
    return seq[n-1]

if __name__ == '__main__':
    for i in range(2,100):
        print fib(i)
