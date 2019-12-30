def print_grid_simple(matrix_2d):
    for j in range(len(matrix_2d[0])):
        for i in range(len(matrix_2d)):
            print(matrix_2d[i][j], end='')
        print()

# Start of program
grid = [
 ['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]
print_grid_simple(grid)