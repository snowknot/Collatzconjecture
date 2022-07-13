cnt = 0
clz = 0
clz_tmp = 0
print("<<콜라츠 추측>>")
print("1. 만약 주어진 수가 짝수라면 2로 나눈다")
print("2. 만약 주어진 수가 홀수라면 3을 곱하고 1을 더한다")
print("3. 위 과정을 반복하다 보면 모든 수는 1로 돌아간다")
print("공식에 사용할 수를 입력해 주세요")
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

print(clztmp, "는 ", cnt, "번 반복하여 1로 돌아갔습니다")
print(" ")
print(" ")
ext = input("> ")
exit