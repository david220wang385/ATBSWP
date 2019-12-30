def printTable(table):
    colwidth = [0] * len(table)
    for i in range(len(table)):
        colwidth[i] = 0

        # Finding longest element in sublists
        for element in table[i]:
            if len(element) > colwidth[i]:
                colwidth[i] = len(element)
        colwidth[i] += 1;
        
    for j in range(len(table[0])):
        for k in range(len(table)):
            print(table[k][j].rjust(colwidth[k]), end='')
        print()


# START HERE
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
printTable(tableData)