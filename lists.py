def compare_fun(lista):
    return lista[2]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = [[3, 5, 3], [2, 9, 8], [2, 3, 7], [4, 1, 5], [3, 2, 1]]
y = x[-3:]
x[-3:] = []
x[:0] = y
print(sorted(z, key=compare_fun, reverse=False))
print(x)
print(z)

x.insert(0, 2)
if 2 in x and x.count(2) == 2: 
    x.remove(2)
    print(x)
