def fact(n):
    if n == 1 or 0:
        return 1
    else:
        factorial = n * fact(n-1)
        return factorial

num = int(input("Enter a number: "))
Factorial = fact(num)
print(f"Factorial of {num} is: {Factorial}")