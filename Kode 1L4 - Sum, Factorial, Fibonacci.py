import os; os.system("cls")

def summ(number):
    result = 0
    for i in range(1, number+1):
        result += i
    return result

def fact(number):
    if number <= 2:
        return number
    else:
        return number * fact(number-1)
    
def fib(number):
    if number < 2:
        return number
    return fib(number-1) + fib(number-2)

exit_condition = 0
while exit_condition == 0:
    user = int(input("Input number: "))
    print(user)

    if user <= 0:
        if user == -1:
            print("Exit Condition!")
            exit_condition = 1
            continue
        print("Number must be positive!")
        continue

    oper = int(input("Choose operation:\n1) Summary\n2) Factorial\n3) Fibonacci\n>> "))
    if oper == 1:
        print(summ(user))
    elif oper == 2:
        print(fact(user))
    elif oper == 3:
        print(fib(user))
    else:
        print("Invalid operator!")
    print("\n")
    
            











