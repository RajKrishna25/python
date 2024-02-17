Rows = int(input("Enter the number of rows for the inverted triangle: "))
for i in range(0, Rows ):    
    for j in range(Rows - i):     
        print(" ", end="")        
    for j in range(0, i + 1):    
        print(i, end=" ")    
    print()