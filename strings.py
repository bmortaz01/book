import string

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
