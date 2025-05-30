#1
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("year must be integer.")
    return(year % 4 ==0 and year % 100!=0) or (year % 400 == 0)

print(is_leap(2025))
print(is_leap(2024))


#2
def check_numbers(n):
    if n % 2 !=0:
        print("weird")
    elif 2 <= n <= 5:
        print("not weird")
    elif 6 <= n <= 20:
        print("weird")
    else:
        print("not weird")

n = int(input("enter a number between (1 <=n <=100): "))

if 1 <=n <=100:
    check_numbers(n)
else:
    print("invalid number, you must use numbers between 1 to 100!!!!!")


#3
def even_numbers_if_else(a, b):
       if a > b:
        a, b = b, a

    if a % 2 != 0:
        a += 1

    if b % 2 != 0:
        b -= 1

    return list(range(a, b + 1, 2))


print(even_numbers_if_else(3, 10)) 

def even_numbers_no_if_else(a, b):
    start = a + (a % 2)  
    end = b - (b % 2)    
    return list(range(min(start, end), max(a, b) + 1, 2))


print(even_numbers_no_if_else(3, 10))  
