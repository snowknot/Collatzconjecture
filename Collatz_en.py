cnt = 0
clz = 0
clz_tmp = 0
print("<<Collatz conjecture>>")
print("1. If the number is even, halve it (ie. divide by two)")
print("2. If the number is odd, triple it and add one.")
print("3. Repeat that, then the number will be 1")
print("Input a number to calculate")
print(" ")
clz = int(input("> "))
clztmp = clz
while True:
    if(clz == 1):
            break
    cnt = cnt + 1
    if(clz%2 == 1):
        clz_tmp = clz
        clz = clz*3
        clz = clz+1
        print(clz_tmp, " x 3 + 1 = ", clz)
        clz_tmp = 0
    else:
        clz_tmp = clz
        clz = clz/2
        print(clz_tmp, " / 2 = ", clz)
        clz_tmp = 0
        if(clz == 1):
            break

print(clztmp, "came back to one repeated ", cnt, " times")
print(" ")
print(" ")
ext = input("> ")
exit