def lower(num_rows):
    print(" ")
    print(" Lower Triangle  ")
    print(" ")
    for i in range(num_rows):
        for j in range(i + 1):
            print('*', end=" ")
        print()
    print(" ")

def upper(num_rows):
    print(" ")
    print(" Upper Triangle  ")
    print(" ")
    for i in range(num_rows):
        for j in range(i, num_rows):
            print("*", end=" ")
        print()
    print(" ")

def pyramid(num_rows):
    print(" ")
    print(" Pyramid  ")
    print(" ")
    for i in range(num_rows):
        for j in range(num_rows - i - 1):
            print(end=" ")
        for j in range(2 * i + 1):
            print('*', end="")
        print()
    print(" ")

num_rows = int(input("Enter The Number Of Rows: "))

pyramid(num_rows)
lower(num_rows)
upper(num_rows)

