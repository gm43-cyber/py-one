num = int(input())
star = "* "
for i in range(1, num + 1):
    for k in range(num - i):
        print(" ", end="")
    for j in range(i):
        print(star, end="")
    print()