import sys
import string
import re


def openFile(infilename, outfilename):
    # print(f'infile={infilename}, outfile={outfilename}')
    punct = str.maketrans('!.,:;-?', '       ')
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for line in infile:
            cleanLine= line.lower()
            cleanLine = cleanLine.translate(punct)
            cleanWords = '\n'.join(cleanLine.split())
            outfile.write(cleanWords)
            outfile.write('\n')

def tasks():
    pattern = re.compile(r'(?P<taskID>\d{3}), (?P<taskTitle>\w+); (?P<taskDesc>.+)')
    with open('tasks.txt') as infile:
        for line in infile:
            line = line.replace('\n', '')
            match = pattern.match(line)
            if match:
                # print(match.groupdict())
                print(f'{'Matched:':<12}{match.group('taskID')}, {match.group('taskTitle')}; {match.group('taskDesc')}')
            else:
                print(f'{'no Match:':<12}{line}')

def match(case=0):
    if case == 0:
        str = '#1$2m_ M\t'
        patterns = [r'\d', r'\D', r'\s', r'\S', r'\w', r'\W', r'.', r'[1mn]']
    elif case == 1:
        str = 'h hi hii hiii hiiii'
        patterns = [r'hi?', r'hi*', r'hi+', r'hi{3}', r'hi{2,3}', 
                    r'hi{2,}', r'hi??', r'hi*?', r'hi+?', r'hi{2,}?']
    elif case == 2:
        pattern = r'\\task'
        texts = ['\task', '\\task', '\\\task', '\\\\task']
    elif case == 3:
        pattern = r'(\w+), (\w+); (\w+)'
        str = 'Homework, urgent; today'
    
    if case >= 0 and case <= 1:
        for pattern in patterns:
            print(f'{pattern: <9}---->    {re.findall(pattern, str)}')
    elif case == 2:
        for text in texts:
            print(f'Match {text!r}: {re.match(pattern, text)}')
    elif case == 3:
        print(re.search(pattern, str))

if __name__ == '__main__':
    func_name = sys.argv[1]     # Capture function name
    params = sys.argv[2:]       # Capture all subsequent arguments
    globals()[func_name](*params)   # Execute function by string name
