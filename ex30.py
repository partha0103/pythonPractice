m = [[1,2,3],[4,5,6],[7,8,9,10]]
print([m[i][i] for i in range(0,3)])
G = (sum(row) for row in m)
print(list(map(sum,m)))
