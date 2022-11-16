# FizzBuzz Rules:
# print numbers frtom 1 to 100
# if number is divisible by 3 , print Fizz
# if number is divisible by 5, print Buzz
# if number divisible by both 3 and 5, print FizzBuzz\
# else print the number

# Example output: 1,2 Fizz, 4,Buzz,Fizz,7,8 Fizz,Buzz,11

for n in range(101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
