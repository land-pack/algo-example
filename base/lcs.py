#coding: utf-8

def LCS(a, b):
    '''''
    输入:a, b: strings
    输出:最大公共子串长度
    复杂度：O(m*n)
    '''
    n = len(a)
    m = len(b)

    l = [([0] * (m + 1)) for i in range(n + 1)]

    for i in range(n + 1)[1:]:
        for j in range(m + 1)[1:]:
            if a[i - 1] == b[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            elif l[i][j - 1] > l[i - 1][j]:
                l[i][j] = l[i][j - 1]
            else:
                l[i][j] = l[i - 1][j]
    return l[n][m]


if __name__ == '__main__':
	lcs = LCS('hellojachska', 'asjndjsl')
	print lcs
