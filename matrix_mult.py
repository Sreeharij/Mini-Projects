rows1,cols1 = list(map(int,input("Enter dimension of 1st matrix(mxn): ").split('x')))
rows2,cols2 = list(map(int,input("Enter dimension of 2nd matrix(mxn): ").split('x')))

if cols1==rows2:
    arr1 = []
    arr2 = []
    print("First Matrix: ")
    for i in range(rows1):
        numbers = list(map(int,input(f"Enter values of {i+1}nd row seperated by space: ").split()))
        arr1.append(numbers)
    print("\nSecond Matrix: ")
    for i in range(rows2):
        numbers = list(map(int,input(f"Enter values of {i+1}nd row seperated by space: ").split()))
        arr2.append(numbers)

    final_matrix = [[0 for i in range(cols2)]for j in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            total = 0
            for k in range(rows2):
                total += arr1[i][k] * arr2[k][j]
            final_matrix[i][j] = total

    print("\n\nResultant Matrix: \n")
    for i in range(rows1):
        for j in range(cols2):
            print(final_matrix[i][j],end=" ")
        print('\n')
else:
    print("Cant do matrix multiplication(incorrect dimensions). ")
