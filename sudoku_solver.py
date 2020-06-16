import random
square_dict = {(0,1,2) : 0 , (3,4,5) : 3, (6,7,8) : 6 }

def make_blank_grid():
    global grid
    grid = []
    for i in range(9):
        grid.append([0,0,0,0,0,0,0,0,0])

def fill_diag_submatrix():
    def diag_square(row,col,initial):
        i=initial
        temp = []
        while i < row:
            j=initial
            while j < col:
                number = random.randint(1,9)
                if number not in temp:
                    temp.append(number)
                    grid[i][j] = number
                    j+=1
            i+=1
    diag_square(3,3,0)
    diag_square(6,6,3)
    diag_square(9,9,6)

def checkGrid(grid,row_and_col):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:

                row_and_col[0] = row
                row_and_col[1] = col

                return False
    return True


def location_is_safe(arr,row,col,number):
    for i in range(9):
        if(arr[row][i] == number):
            return False

    for i in range(9):
        if(arr[i][col] == number):
            return False

    for keys in square_dict.keys():
        if row in keys:
            row_start = square_dict[keys]
        if col in keys:
            col_start = square_dict[keys]

    square = [arr[i][col_start:col_start+3] for i in range(row_start,row_start+3)]

    if number in (square[0]+square[1]+square[2]):
        return False
    return True

def solve_grid(arr):

    row_and_col = [0,0]

    if checkGrid(arr,row_and_col):
        return True

    row = row_and_col[0]
    col = row_and_col[1]

    for number in range(1, 10):

        if(location_is_safe(arr, row, col, number)):
            arr[row][col]= number
            if(solve_grid(arr)):
                return True
            else:
                arr[row][col] = 0
    else:
        return False

def print_grid():
    def format_grid(grid):
        print('|--------|---------|---------|')
        for i in grid:
            print("| ",end="")
            for value in i[0:3]:
                print(value,end=" ")
            print(" | ",end=" ")
            for value in i[3:6]:
                print(value,end=" ")
            print(" | ",end=" ")
            for value in i[6:9]:
                print(value,end=" ")
            print(" |")

    format_grid(grid[0:3])
    format_grid(grid[3:6])
    format_grid(grid[6:9])
    print('|________|_________|_________|')

def main():
    make_blank_grid()
    fill_diag_submatrix()
    if solve_grid(grid):
        print_grid()
    else:
        print('No solutions!')
if __name__=='__main__':
    main()
