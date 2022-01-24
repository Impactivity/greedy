import sys
read = sys.stdin.readline

num = int(read())

change = 1000 - num

money = [500,100,50,10,5,1]
cnt = 0
inx = 0
while change != 0:
    if inx > len(money) - 1 :
        break

    if change >= money[inx]:
        change = change - money[inx]
        cnt += 1
    else:
        inx += 1
print(cnt)
