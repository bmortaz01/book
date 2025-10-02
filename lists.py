import sys
import copy
from collections.abc import Hashable
from collections import deque
from timeit import timeit


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

def isHashable():
    print(f'{'Data': <21}   {'Data Type': <21}   {'Hashable'}')
    items = [{'a':1}, 
             [[0,1], [1,2], [2,3]],
             [1,2,3], {1,2,3}, 
             ('tom', [1, 2, 3]), 
             ("filename", "extension"), 
             (1,2,3), 
             frozenset([1,2,3]), 
             bytes(1), bytearray(b'A\x00\x00\x00\x00'), 
             complex(3,5),
             1, 1.2, "test", True, None]
    for item in items:
        print(f'{str(item): <21}   {str(type(item)): <21} | {isinstance(item, Hashable)}')

def compListsSets():
    for count in [10, 100, 1000, 10000, 100000]:
        str_setup = f"from random import randint; n = {count}; " \
                f"set_numbers = set(range(n)); " \
                f"list_numbers = list(range(n))"
        set_stmt = "randint(0, n-1) in set_numbers"
        list_stmt = "randint(0, n-1) in list_numbers"
        time_set = timeit(set_stmt, setup=str_setup, number=10000)
        time_list = timeit(list_stmt, setup=str_setup, number=10000)
        print(f"{count: >6}: set - {time_set:e} Sec vs. list - {time_list:e} Sec")

def containedIn(personal, recommended):
    for stock in personal:
        if stock not in recommended:
            return False
    return True

def setRelations():
    stocks = {'AAPL', 'GOOG', 'AMZN', 'NVDA'}
    client0 = {'GOOG', 'AMZN'}
    client1 = {'AMZN', 'SNAP'}
    print(f'Is {str(client0): <19} contained in {str(stocks): <40} | {containedIn(client0, stocks)}')
    print(f'Is {str(client1): <19} contained in {str(stocks): <40} | {containedIn(client1, stocks)}')
    print(f'Is {str(client0): <19} contained in {str(stocks): <40} | {len(client0 & stocks) == len(client0)}')
    print(f'Is {str(client1): <19} contained in {str(stocks): <40} | {len(client1 & stocks) == len(client1)}')
    print(f'Is {str(stocks): <40} is superset  {str(client0): <19}| {stocks.issuperset(client0)}')
    print(f'Is {str(client1): <19} is subset {str(stocks): <40} | {client1.issubset(stocks)}')
    print(f'{str(client1): <19} {'Union(|)': <19} {str(stocks): <40} == {str(client1 | stocks)}')
    print(f'{str(client1): <19} {'Intersection(&)': <19} {str(stocks): <40} == {str(client1 & stocks)}')
    print(f'{str(client1): <19} {'Sym Diff(^)': <19} {str(stocks): <40} == {str(client1 ^ stocks)}')
    print(f'{str(client1): <19} {'Diff(-)': <19} {str(stocks): <40} == {str(client1 - stocks)}')    

def timeFifo(*nums):
    for num in nums:
        n = int(num)
        x = list(range(n))
        y = deque(range(n))
        t_1 = timeit(lambda: x.pop(0), number=n)
        t_2 = timeit(lambda: y.popleft(), number=n)
        print(f"{n: >9} list: {t_1:.6e} | deque: {t_2:.6e}")

if __name__ == '__main__':
    func_name = sys.argv[1]     # Capture function name
    params = sys.argv[2:]       # Capture all subsequent arguments
    globals()[func_name](*params)   # Execute function by string name
    