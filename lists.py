import sys
import copy
from collections.abc import Hashable, Iterable
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

def isHashable(isIt: str = 'Hashable', strSort: str = False):
    doSort = bool(strSort)
    header1 = {'IsIt': None}
    match isIt:
        case 'Hashable':
            header1['IsIt'] = f'{'Is Hashable': <11}'
        case 'Iterable':
            header1['IsIt'] = f'{'Is Iterable': <11}'
        case _:
            print("Usage: isHashable {Hashable | Iterator}")
            return

    header1.update({'Row': f'{'#': ^4}', 'Data': f'{'Data': ^41}', 'Type': f'{'Data Type': ^21}', 
                    'Desc':f'{'Description': ^31}'})
    header2 = {'Row': f'{'-':-<4}', 'Data': f'{'-':-^41}', 'Type': f'{'-':-^21}', 'IsIt': f'{'-':-<11}', 'Desc':f'{'-':-^31}'}
    print(f'{header1['Row']} | {header1['Data']}   | {header1['Type']} | {header1['IsIt']} | {header1['Desc']}')
    print(f'{header2['Row']}   {header2['Data']}     {header2['Type']}   {header2['IsIt']}   {header2['Desc']}')
    
    items = [
            {'Data': {'a':1},               'Desc': 'Dictionary, Mutable'},
            {'Data': [[0,1], [1,2], [2,3]], 'Desc': 'List of lists, Mutable'},
            {'Data': [1,2,3],               'Desc': 'List, Mutable'},
            {'Data': {1,2,3},               'Desc': 'Set, Mutable'},
            {'Data': ('tom', [1, 2, 3]),    'Desc': 'Tuple, Non-Mutable'},
            {'Data': ("filename", "extension"), 'Desc': 'Tuple, Non-Mutable'},
            {'Data': (1,2,3),               'Desc': 'Tuple, Non-Mutable'},
            {'Data': frozenset([1,2,3]),    'Desc': 'Frozen-Set, Non-Mutable'},
            {'Data': bytes(1),              'Desc': 'Bytes, Non-Mutable'},
            {'Data': bytearray(b'A\x00\x00\x00\x00'), 'Desc': 'Byte Array, Mutable'},
            {'Data': map(str, [1, 2, 3]),   'Desc': "Map, Iterator, Non-Mutable -- map(str, [1, 2, 3])"},
            {'Data': zip([1,2], ('a','b')), 'Desc': "Zip, Iterator, Non-Mutable -- zip([1,2], ('a','b'))"},
            {'Data': filter(bool, (-2, -1, 0, 1, 2)), 'Desc': "Filter, Iterator, Non-Mutable -- zip([1,2], ('a','b'))"},
            {'Data': enumerate([1, 2, 3]),  'Desc': "Enumerate, Enumerator, Non-Mutable -- enumerate([1, 2, 3])"},
            {'Data': reversed('Hello'),     'Desc': "Reversed, Iterator, Non-Mutable -- reversed('Hello')"},
            {'Data': complex(3,5),          'Desc': 'Complex, Non-Mutable'},
            {'Data': 1,                     'Desc': 'Integer, Non-Mutable'},
            {'Data': 1.2,                   'Desc': 'Float, Non-Mutable'},
            {'Data': "test",                'Desc': 'String, Non-Mutable'},
            {'Data': True,                  'Desc': 'Boolean, Non-Mutable'},
            {'Data': None,                  'Desc': 'NoneType, Non-Mutable'}
        ]

    sortedList = items
    match (isIt, doSort):
        case ('Hashable', True):
            sortedList = sorted(items, key=lambda x: isinstance(x['Data'], Hashable))
        case ('Iterable', True):
            sortedList = sorted(items, key=lambda x: isinstance(x['Data'], Iterable))

    for i, item in enumerate(sortedList):
        data = item['Data']
        desc = item['Desc']
        match isIt:
            case 'Hashable':
                print(f'{i: ^4} | {str(data): <41}   | {str(type(data)): <21} | {str(isinstance(data, Hashable)): ^11} | {desc}')
            case 'Iterable':
                print(f'{i: ^4} | {str(data): <41}   | {str(type(data)): <21} | {str(isinstance(data, Iterable)): ^11} | {desc}')

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
    