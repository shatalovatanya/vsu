fib1 = 1
fib2 = 1
endWhile = int(input("Значение какого элемента ряда \
Фибоначчи вы хотите узнать? \n"))
counter = 2
while counter < endWhile:
    fibSum = fib2 + fib1
    fib1 = fib2
    fib2 = fibSum
    counter += 1
print(fibSum)