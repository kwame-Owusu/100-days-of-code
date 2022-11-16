# simple code to showcase how recursion works in pytohn.

def display_hello(i):
    if i > 0:
        print("hello world")
        display_hello(i - 1)


# here showcasing how the while loop works
i = 0

while i < 3:
    print("hello world")
    i += 1
