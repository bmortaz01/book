import sys
import copy

def greet(name):
    print(f"Hello, {name}!")

def compare_fun(lista):
    return lista[2]

def test_lists():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = x[-3:]
    z = [[3, 5, 3], [2, 9, 8], [2, 3, 7], [4, 1, 5], [3, 2, 1]]
    x[-3:] = []
    x[:0] = y
    print('z             -> ', z)
    print('z[?][2] sorted -> ', sorted(z, key=compare_fun, reverse=False))
    print('x -> ', x)

    x.insert(0, 2)
    if 2 in x and x.count(2) == 2: 
        x.remove(2)
        print('x -> ', x)

    a = copy.deepcopy(z)
    a[0][0] = 0
    print('a == deepcopy(z) -> ', a)
    print('z                -> ', z)

if __name__ == '__main__':
    func_name = sys.argv[1]     # Capture function name
    params = sys.argv[2:]       # Capture all subsequent arguments
    globals()[func_name](*params)   # Execute function by string name
    