nth = int(input("How many terms would you like?: "))
x = 0
y = 1
count = 2
term = [0 , 1]

if nth <= 0:
    print("Enter a positive integer")
elif nth == 1:
    print("Fibonacci Sequence: ")
    print(x)
elif nth == 2:
    print("Fibonacci Sequence: ")
    print(term)
else:
    print("Fibonacci Sequence: ")
    while count <= nth:
        terms = x + y
        term.append(terms)
        x = y
        y = terms
        count += 1
    print(term)