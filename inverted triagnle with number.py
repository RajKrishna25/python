Rows = int(input("Enter the number of rows for the pyramid: "))
Num = 0 
for i in range(0, Rows + 1): 
    for j in range(Rows - i):
        print(" ", end="")
    for j in range(Num, Num + i):
        print(j, end=" ")
    Num += i

    print("")

